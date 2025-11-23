from .constant import BROWSER_PROTOCOL_URL, JS_PROTOCOL_URL
from .method_generator import MethodGenerator
from .event_generator import EventGenerator
from .type_generator import TypeGenerator
from .client_generator import ClientGenerator
from jinja2_strcase import StrcaseExtension
from jinja2 import Environment
from textwrap import dedent
from functools import cache
from pathlib import Path
from typing import Any
import inflection
import httpx

class CDPGenerator:    
    def __init__(self):
        self.path = Path("./protocol")
        self.env=Environment(trim_blocks=True,lstrip_blocks=True,extensions=[StrcaseExtension])
        self.type_generator = TypeGenerator(path=self.path)
        self.event_generator = EventGenerator(path=self.path)
        self.method_generator = MethodGenerator(path=self.path)
        self.client_generator = ClientGenerator()

    @property
    @cache
    def domains(self)->list[dict[str,Any]]:
        domains=[]
        for url in [BROWSER_PROTOCOL_URL,JS_PROTOCOL_URL]:
            try:
                protocol=httpx.get(url).json()
                domains.extend(protocol.get('domains',[]))
            except Exception as e:
                print(f"Failed to load protocol from {url}: {e}")
        return domains

    def generate(self):
        self.generate_protocol()
        self.generate_client()
    
    def generate_protocol(self):
        for domain in self.domains:
            if not domain.get('deprecated',False):
                self.generate_domain_types(domain)
                self.generate_domain_services(domain)
    
    def generate_client(self):
        client_dir=Path("./client")
        domains=list(filter(lambda x: not x.get('deprecated',False),self.domains))
        methods_content=self.client_generator.generate_methods(domains)
        # events_content=self.client_generator.generate_events(domains)

        self.write_file(client_dir / "methods.py",methods_content)
        # self.write_file(client_dir / "events" / "__init__.py",events_content)

    def generate_domain_services(self,domain:dict):
        domain_dir = self.path / inflection.underscore(domain['domain'])

        event_services_content=self.event_generator.generate_event_services(domain)
        method_services_content=self.method_generator.generate_method_services(domain)

        self.write_file(domain_dir/"events"/"service.py",event_services_content)
        self.write_file(domain_dir/"methods"/"service.py",method_services_content)

    def generate_domain_types(self,domain:dict):
        domain_dir = self.path / inflection.underscore(domain['domain'])

        types_content=self.type_generator.generate_types(domain)
        event_types_content=self.event_generator.generate_event_types(domain)
        method_types_content=self.method_generator.generate_method_types(domain)

        self.write_file(domain_dir / "__init__.py",'')
        self.write_file(domain_dir / "events" / "__init__.py",'')
        self.write_file(domain_dir / "methods" / "__init__.py",'')

        self.write_file(domain_dir / "types.py",types_content)
        self.write_file(domain_dir / "events" / "types.py",event_types_content)
        self.write_file(domain_dir / "methods" / "types.py",method_types_content)

    def write_file(self,path:Path,content:str):
        dir=path.parent
        dir.mkdir(exist_ok=True,parents=True)
        path.write_text(content)