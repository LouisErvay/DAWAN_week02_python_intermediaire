from media_factory.i_media_factory import IMediaFactory
from media.book import Book

class BookFactory(IMediaFactory):
    def __init__(self):
        pass

    def create_media(self, name: str, author: str, available: bool) -> Book:
        return Book(name=name, author=author, available=available)