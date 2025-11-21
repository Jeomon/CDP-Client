

class EventGenerator:
    def generate_events(self,domain:dict):
        domain_name=domain.get('domain')
        events=domain.get('events',[])