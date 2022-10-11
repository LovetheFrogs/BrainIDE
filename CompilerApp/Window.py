class Window:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        
    @abstractmethod
    def get_name(self):
        pass
