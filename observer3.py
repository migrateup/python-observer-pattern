class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Publisher:
    def __init__(self, events):
        # maps event names to subscribers
        # str -> dict
        self.events = { event : dict()
                          for event in events }
    def subscribers(self, event):
        return self.events[event]
    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.subscribers(event)[who] = callback
    def unregister(self, event, who):
        del self.subscribers(event)[who]
    def dispatch(self, event, message):
        for subscriber, callback in self.subscribers(event).items():
            callback(message)
        
