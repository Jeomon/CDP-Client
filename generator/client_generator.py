from jinja2_strcase import StrcaseExtension
from jinja2 import Environment
from textwrap import dedent

class ClientGenerator:
    def __init__(self):
        self.env=Environment(trim_blocks=True,lstrip_blocks=True,extensions=[StrcaseExtension])

    def generate_methods(self,domains:list[dict]):
        template_str = dedent('''
            """CDP Methods"""
            from typing import TYPE_CHECKING, Any, Dict, Optional
            
            if TYPE_CHECKING:
                from .service import CDPClient

            class CDPMethods:
                def __init__(self, client: "CDPClient"):
                    self.client = client

                async def send(self, method: str, params: Optional[Dict[str, Any]] = None,session_id: Optional[str] = None) -> Any:
                    return await self.client.send(method, params,session_id)

                {% for domain in domains %}
                @property
                def {{ domain['domain'] | to_snake }}(self):
                    from protocol.{{ domain['domain'] | to_snake }}.methods.service import {{ domain['domain'] }}Methods
                    return {{ domain['domain'] }}Methods(methods=self)

                {% endfor %}
        ''')
        template=self.env.from_string(template_str)
        code = template.render(domains=domains)
        return dedent(code)

    def generate_events(self,domains:list[dict]):
        template_str = dedent('''
            """CDP Events"""
            from typing import TYPE_CHECKING, Callable, Any
            
            if TYPE_CHECKING:
                from .service import CDPClient

            class CDPEvents:
                def __init__(self, client: "CDPClient"):
                    self.client = client

                def on(self, event: str, callback: Callable[[Any], None]) -> None:
                    self.client.on(event, callback)

                {% for domain in domains %}
                @property
                def {{ domain['domain'] | to_snake }}(self):
                    from protocol.{{ domain['domain'] | to_snake }}.events.service import {{ domain['domain'] }}Events
                    return {{ domain['domain'] }}Events(events=self)
                    
                {% endfor %}
        ''')

        template=self.env.from_string(template_str)
        code = template.render(domains=domains)
        return dedent(code)