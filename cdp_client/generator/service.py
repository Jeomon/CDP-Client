from cdp_client.generator.constant import BROWSER_PROTOCOL_URL
from cdp_client.generator.method_generator import MethodGenerator
from cdp_client.generator.type_generator import TypeGenerator
from cdp_client.generator.event_generator import EventGenerator
from jinja2 import Template
from textwrap import dedent
from pathlib import Path
import httpx

def load_protocol():
    return httpx.get(BROWSER_PROTOCOL_URL).json()

class CDPGenerator:
    def __init__(self,output_dir:Path=Path("./cdp_client/protocol")):
        self.output_dir = output_dir
        self.protocol = load_protocol()
        self.method_generator = MethodGenerator()
        self.type_generator = TypeGenerator()
        self.event_generator = EventGenerator()
    
    def generate(self):
        for domain in self.protocol['domains']:
            self.generate_domain_types(domain)
            self.generate_domain_service(domain)

    def generate_domain_service(self,domain:dict):
        domain_dir = self.output_dir / domain['domain'].lower()
        event_services_content=self.event_generator.generate_event_services(domain)
        method_services_content=self.method_generator.generate_method_services(domain)

        self.write_file(domain_dir/"events"/"service.py",event_services_content)
        self.write_file(domain_dir/"methods"/"service.py",method_services_content)

    def generate_domain_types(self,domain:dict):
        domain_dir = self.output_dir / domain['domain'].lower()
        inits_content=self.generate_inits(domain)
        types_content=self.type_generator.generate_types(domain)
        event_types_content=self.event_generator.generate_event_types(domain)
        method_types_content=self.method_generator.generate_method_types(domain)

        self.write_file(domain_dir / "types.py",types_content)
        self.write_file(domain_dir / "__init__.py",inits_content)
        self.write_file(domain_dir / "events" / "types.py",event_types_content)
        self.write_file(domain_dir / "methods" / "types.py",method_types_content)

    def generate_inits(self,domain:dict):
        template_str=dedent('''
        """CDP {{domain}} Domain"""

        from .events.types import *
        from .methods.types import *
        from .types import *
        ''').strip()
        template=Template(template_str,trim_blocks=True,lstrip_blocks=True)
        code=template.render(domain=domain['domain'])
        return dedent(code)

    def write_file(self,path:Path,content:str):
        dir=path.parent
        dir.mkdir(exist_ok=True,parents=True)
        path.write_text(content)