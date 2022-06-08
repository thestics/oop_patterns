class EventListener:
    def update(self, data: str):
        pass

class 


class FileReader:
    def __init__(self, path):
        self.path = path
        self.listeners = {}
        
    def subscribe(self, event_type: str, listener: EventListener):
        self.listeners[event_type] = listener
    
    def unsubscribe(self, event_type: str, listener: EventListener):
        self.listeners.pop(event_type)
