class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Publisher:
    def __init__(self, channels):
        # maps channel names to subscribers
        # str -> dict
        self.channels = { channel : dict()
                          for channel in channels }
    def subscribers(self, channel):
        return self.channels[channel]
    def register(self, channel, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.subscribers(channel)[who] = callback
    def unregister(self, channel, who):
        del self.subscribers(channel)[who]
    def dispatch(self, channel, message):
        for subscriber, callback in self.subscribers(channel).items():
            callback(message)
        
