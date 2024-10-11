from medias.Book import Book
from medias.Magazine import Magazine

class MediaFactory:

    def __init__(self) -> None:
        pass

    @staticmethod
    def create_media(title, author, type):
        if type.lower() == "book":
            return Book(title, author)
        elif type.lower() == "magazine":
            return Magazine(title, author)
        else:
            raise ValueError("Invalid type of media")