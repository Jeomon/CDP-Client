from textwrap import dedent
from jinja2 import Template

class MethodGenerator:
    def __init__(self):
        self.current_domain:str=None
        self.imports=set()
        self.generated_methods=set()
        self.type_checking_imports=set()

    def clear(self):
        self.imports.clear()
        self.generated_methods.clear()
        self.type_checking_imports.clear()

    def generate_method_services(self,domain:dict):
        self.current_domain=domain.get('domain')
        methods=domain.get('commands',[])

        method_implementations = [self.generate_method_implementation(method) for method in methods]

        template_str = dedent('''
            """CDP {{ domain_name }} Methods"""

            from cdp_client.methods import CDPMethods
            from typing import TypedDict,Optional
            from .types import *

            class {{ domain_name }}Methods:
                {% if method_implementations | length > 0 %}
                def __init__(self, methods:CDPMethods):
                    self.methods = methods
                {% for implementation in method_implementations %}
                {{ implementation | indent(4) }}
                {% endfor %}
                {% else %}
                pass
                {% endif %}
        ''')

        template = Template(template_str, trim_blocks=True, lstrip_blocks=True)
        code = template.render(
            domain_name=self.current_domain,
            method_implementations=method_implementations,
        )
        return code

    def generate_method_implementation(self,method:dict):
        method_name=method.get('name')
        parameters=method.get('parameters',[])
        return_parameters=method.get('returns',[])

        template_str = dedent('''
        async def {{ method_name }}(self, params: {% if parameters|length > 0 %}Optional[{{ method_name }}Parameters]{% else %}None{% endif %}=None) -> {% if return_parameters|length > 0 %}{{ method_name }}Returns{% else %}Dict[str, Any]{% endif %}:
            return await self.methods._send(method="{{ domain_name }}.{{ method_name }}", params=params)
        ''')

        template = Template(template_str, trim_blocks=True, lstrip_blocks=True)
        code = template.render(
            domain_name=self.current_domain,
            method_name=method_name,
            parameters=parameters,
            return_parameters=return_parameters,
        )
        return code

    def generate_method_types(self,domain:dict):
        self.current_domain=domain.get('domain')
        methods=domain.get('commands',[])

        self.clear()

        self.imports.add("from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple")

        for method in methods:
            self.generated_methods.add(method.get('name'))

        parameter_definitions_code=[self.generate_parameter_definition(method) for method in methods]
        return_definitions_code=[self.generate_return_definition(method) for method in methods]

        template_str = dedent('''
            """CDP {{ domain_name }} Methods Types"""

            {% for import_ in imports %}
            {{ import_ }}
            {% endfor %}
            {% if type_checking_imports %}

            from typing import TYPE_CHECKING
            if TYPE_CHECKING:
                {% for type_checking_import in type_checking_imports %}
                {{ type_checking_import }}
                {% endfor %}
            {% endif %}

            {% for definition in parameter_definitions_code %}
            {{ definition }}
            {% endfor %}
            {% for definition in return_definitions_code %}
            {{ definition }}
            {% endfor %}            
        ''')

        template = Template(template_str, trim_blocks=True, lstrip_blocks=True)
        code = template.render(
            domain_name=self.current_domain,
            parameter_definitions_code=parameter_definitions_code,
            return_definitions_code=return_definitions_code,
            imports=sorted(filter(lambda x: not x.startswith(f'from ..{self.current_domain}.types import'),self.imports)),
            type_checking_imports=sorted(self.type_checking_imports),
        )
        return dedent(code)
    
    def generate_parameter_definition(self, method_definition:dict):
        method_name=method_definition.get('name')
        parameters=method_definition.get('parameters',[])
        if not parameters:
            return ''

        required_parameters=[]
        optional_parameters=[]

        for parameter in parameters:
            parameter['type'] = self.resolve_parameter_type(parameter)
            if parameter.get('optional',False):
                optional_parameters.append(parameter)
            else:
                required_parameters.append(parameter)

        if optional_parameters and not required_parameters:
            total=False
        else:
            total=True

        template_str = dedent('''
        class {{ method_name }}Parameters(TypedDict, total={{ total }}):
            {% if not required_parameters and not optional_parameters %}
            pass
            {% else %}
            {% if required_parameters %}
            {% for parameter in required_parameters %}
            {{ parameter['name'] }}: {{ parameter['type'] }}
            {% if parameter['description'] %}
            """{{ parameter['description'] | replace('\n', ' ') | replace('`', '') }}"""
            {% endif %}
            {% endfor %}
            {% endif %}
            {% if optional_parameters %}
            {% for parameter in optional_parameters %}
            {{ parameter['name'] }}: NotRequired[{{ parameter['type'] }}]
            {% if parameter['description'] %}
            """{{ parameter['description'] | replace('\n', ' ') | replace('`', '') }}"""
            {% endif %}
            {% endfor %}
            {% endif %}
            {% endif %}
        ''')
        
        template=Template(template_str,trim_blocks=True,lstrip_blocks=True)
        code=template.render(
            total=total,
            method_name=method_name,
            required_parameters=required_parameters,
            optional_parameters=optional_parameters,
        )
        self.generated_methods.add(method_name)
        return dedent(code)

    def generate_return_definition(self, method_definition:dict):
        method_name=method_definition.get('name')
        return_parameters=method_definition.get('returns',[])
        if not return_parameters:
            return ""
        
        for return_parameter in return_parameters:
            return_parameter['type']=self.resolve_parameter_type(return_parameter)

        template_str = dedent('''
        class {{ method_name }}Returns(TypedDict):
            {% if not return_parameters %}
            pass
            {% else %}
            {% for return_parameter in return_parameters %}
            {{ return_parameter['name'] }}: {{ return_parameter['type'] }}
            {% if return_parameter['description'] %}
            """{{ return_parameter['description'] | replace('\n', ' ') | replace('`', '') }}"""
            {% endif %}
            {% endfor %}
            {% endif %}
        ''')

        template=Template(template_str,trim_blocks=True,lstrip_blocks=True)
        code=template.render(
            method_name=method_name,
            return_parameters=return_parameters
        )
        self.generated_methods.add(method_name)
        return dedent(code)
        
    def resolve_parameter_type(self, parameter:dict):
        if "$ref" in parameter:
            return self.resolve_type_reference(parameter)
        
        parameter_type=parameter.get("type","any")
        match parameter_type:
            case 'object':
                return "Dict[str, Any]"
            case 'array':
                items=parameter.get('items',{})
                return f"List[{self.resolve_type_reference(items) if '$ref' in items else self.map_primitive_type(items.get('type'))}]"
            case 'string':
                if 'enum' in parameter:
                    return f"Literal[{', '.join(f'"{v}"' for v in parameter.get('enum'))}]"
                else:
                    return "str"
            case _:
                return self.map_primitive_type(parameter_type)

    def resolve_type_reference(self, type_ref:dict):
        ref=type_ref.get('$ref')
        if '.' in ref:
            parts=ref.split('.')
            domain=parts[0].lower()
            type_name=parts[1]
            
            # Imports from cross domain
            self.type_checking_imports.add(f"from ..{domain}.types import {type_name}")
            return type_name
        else:
            # Imports from same domain
            self.type_checking_imports.add(f"from .types import {ref}")
            return ref

    def map_primitive_type(self, type_name: str):
        match type_name:
            case "string":
                return "str"
            case "object":
                return "Dict[str, Any]"
            case "number":
                return "float"
            case "integer":
                return "int"
            case "boolean":
                return "bool"
            case _:
                return "Any"
        