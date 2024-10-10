from media_factory.i_media_factory import IMediaFactory
from media.movie import Movie

class MovieFactory(IMediaFactory):
    def __init__(self):
        pass

    def create_media(self, name: str, author: str, available:bool) -> Movie:
        return Movie(name=name, author=author, available=available)