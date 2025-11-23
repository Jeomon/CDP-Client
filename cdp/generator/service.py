from .constant import BROWSER_PROTOCOL_URL, JS_PROTOCOL_URL
from .method_generator import MethodGenerator
from .event_generator import EventGenerator
from .type_generator import TypeGenerator
from jinja2 import Template
from textwrap import dedent
from pathlib import Path
from typing import Any
import inflection
import httpx

class CDPGenerator:
    def __init__(self,path:Path=Path("./protocol")):
        self.path = path
        self.type_generator = TypeGenerator(path=path)
        self.event_generator = EventGenerator(path=path)
        self.method_generator = MethodGenerator(path=path)

    @property
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
        for domain in self.domains:
            if not domain.get('deprecated',False):
                self.generate_domain_types(domain)
                self.generate_domain_services(domain)

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