from medias.IMedia import IMedia

class Magazine(IMedia):

    def __init__(self, title:str, author:str) -> None:
        self.title = title
        self.author = author
        self.is_available = True
        self.observers = []
        
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_media_type(self):
        return "Magazine"
    
    def is_available(self):
        return self.is_available
        
    def set_available(self, available):
        self.is_available = available
        if self.is_available:
            self.notify()

    def __str__(self) -> str:
        return f"{self.title} de {self.author}"
    
