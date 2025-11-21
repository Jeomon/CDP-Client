from cdp_client.generator.constant import BROWSER_PROTOCOL_URL
from cdp_client.generator.method_generator import MethodGenerator
from cdp_client.generator.type_generator import TypeGenerator
from cdp_client.generator.event_generator import EventGenerator
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
            self.generate_domain(domain)

    def generate_domain(self,domain:dict):
        domain_dir = self.output_dir / domain['domain'].lower()
        domain_dir.mkdir(exist_ok=True,parents=True)
        
        types_content=self.type_generator.generate_types(domain)
        events_content=self.event_generator.generate_events(domain)
        methods_content=self.method_generator.generate_methods(domain)

        self.write_file(domain_dir / "types.py",types_content)
        self.write_file(domain_dir / "events.py",events_content)
        self.write_file(domain_dir / "methods.py",methods_content)

    def write_file(self,path:Path,content:str):
        path.write_text(content)