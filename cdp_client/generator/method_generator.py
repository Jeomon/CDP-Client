class MethodGenerator:

    def generate_methods(self,domain:dict):
        domain_name=domain.get('domain')
        methods=domain.get('commands',[])