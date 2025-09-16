class Media:

    def __init__(self, id, web_url, creator, rotation=0, brightness=100, skew="1, 0, 0, 1, 0, 0", gradient=False, gradient_colors="#e66465, #000000"):
        self.id = id
        self.web_url = web_url
        self.creator = creator
        self.rotation = rotation
        self.brightness = brightness
        self.skew = skew
        self.gradient = gradient
        self.gradient_colors = gradient_colors

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Media({self.id}, {self.web_url}, {self.creator}, {self.rotation}, {self.brightness}, {self.skew}, {self.gradient}, {self.gradient_colors})"