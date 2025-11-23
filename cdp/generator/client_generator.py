from jinja2_strcase import StrcaseExtension
from jinja2 import Environment
from textwrap import dedent

class ClientGenerator:
    def __init__(self):
        self.env=Environment(trim_blocks=True,lstrip_blocks=True,extensions=[StrcaseExtension])

    def generate_methods(self,domains:list[dict]):
        template_str = dedent('''
            """CDP Methods"""

            class CDPMethods:

                {% for domain in domains %}
                @property
                def {{ domain['domain'] | to_snake }}(self):
                    from ..protocol.{{ domain['domain'] | to_snake }}.methods.service import {{ domain['domain'] }}Methods
                    return {{ domain['domain'] }}Methods(methods=self)
                {% endfor %}
        ''')
        template=self.env.from_string(template_str)
        code = template.render(domains=domains)
        return dedent(code)

    def generate_events(self,domains:list[dict]):
        pass