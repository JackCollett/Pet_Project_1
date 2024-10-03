class Media:

    def __init__(self, id, photo_url):
        self.id = id
        self.photo_url = photo_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"({self.id}, {self.photo_url})"