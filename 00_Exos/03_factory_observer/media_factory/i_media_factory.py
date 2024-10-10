from abc import ABC, abstractmethod
from media.i_media import IMedia

class IMediaFactory(ABC):

    @abstractmethod
    def create_media(self, name: str, author: str, available:bool) -> IMedia:
        pass