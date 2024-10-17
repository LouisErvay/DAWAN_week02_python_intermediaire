from medias.IMedia import IMedia
from observers.IObserver import IObserver

class User(IObserver):

    def __init__(self, firstname:str, lastname:str):
        self.firstname = firstname
        self.lastname = lastname

    def update(self, media: IMedia):
        print(f"{self.firstname}! Un média est disponible et n'attend que vous: {media}!")