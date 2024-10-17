class Media:

    def __init__(self, id, web_url):
        self.id = id
        self.web_url = web_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"({self.id}, {self.web_url})"