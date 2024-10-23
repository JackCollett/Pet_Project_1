class Media:

    def __init__(self, id, web_url, rotation=0, brightness=1):
        self.id = id
        self.web_url = web_url
        self.rotation = rotation
        self.brightness = brightness

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Media({self.id}, {self.web_url})"
    
    def apply_rotation(self, degrees):
        self.rotation += degrees
        
    def apply_brightness(self, factor):
        self.apply_brightness = factor