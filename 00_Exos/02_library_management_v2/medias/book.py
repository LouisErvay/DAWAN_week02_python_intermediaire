import sys

from medias.i_media import IMedia

class Book(IMedia):
    def __init__(self,id: int,  name: str, author: str, status: bool):
        self.id = id
        self.name: str = name
        self.author: str = author
        self.status: bool = status


    def get_name(self) -> str:
        return self.name

    def set_name(self, name) -> None:
        self.name = name

    def get_author(self) -> str:
        return self.author

    def set_author(self, author) -> None:
        self.author = author

    def get_status(self) -> bool:
        return self.status

    def set_status(self, status) -> None:
        self.status = status