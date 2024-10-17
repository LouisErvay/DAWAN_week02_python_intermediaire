from medias.IMedia import IMedia

class Book(IMedia):
    
    def __init__(self, title:str, author:str) -> None:
        self.title = title
        self.author = author
        self.is_available = True

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_media_type(self):
        return "Book"
    
    def is_available(self):
        return self.is_available
        
    def set_available(self, available):
        self.is_available  = available

    def __str__(self) -> str:
        return f"{self.title} par {self.author}"