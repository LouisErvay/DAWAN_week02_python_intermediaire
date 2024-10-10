from observer.i_observer import IObserver

from media.i_media import IMedia

class User(IObserver):
    def __init__(self, name):
        self.name = name

    def media_available(self, media:IMedia):
        print(f"Notification pour {self.name}: Le média: {media.get_name()} est disponible !")