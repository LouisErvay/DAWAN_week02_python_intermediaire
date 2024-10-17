from media.i_media import IMedia

from observer.i_subject import ISubject
from observer.i_observer import IObserver

class Book(IMedia, ISubject):
    def __init__(self, name: str, author: str, available: bool):
        self.media_type = "book"
        self.observers: [IObserver] = []

        self.name = name
        self.author = author
        self.available = available

    def get_name(self):
        return self.name

    def set_available(self, available: bool):
        self.available = available
        if available == True:
            self.notify()

    def attach(self, observer: IObserver):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: IObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.media_available(media=self)