from medias.IMedia import IMedia

class Magazine(IMedia):

    def __init__(self, title:str, author:str) -> None:
        self.title = title
        self.author = author
        self.is_available = True
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_media_type(self):
        return "Magazine"
    
    def is_available(self):
        return self.is_available
        
    def set_available(self, available):
        self.is_available  = available
    
