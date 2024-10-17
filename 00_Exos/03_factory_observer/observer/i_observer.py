from abc import ABC, abstractmethod

from media.i_media import IMedia

class IObserver(ABC):

    @abstractmethod
    def media_available(self, media: IMedia):
        pass