class Media:

    def __init__(self, id, web_url, rotation=0, brightness=100):
        self.id = id
        self.web_url = web_url
        self.rotation = rotation
        self.brightness = brightness

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Media({self.id}, {self.web_url}, {self.rotation}, {self.brightness})"