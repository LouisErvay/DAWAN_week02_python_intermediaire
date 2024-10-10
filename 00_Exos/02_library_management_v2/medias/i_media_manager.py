from abc import ABC, abstractmethod

from medias.i_media import IMedia
from users.user import User

class IMediaManager(ABC):

    @abstractmethod
    def add_media(self, media: IMedia):
        pass

    @abstractmethod
    def loan_media(self, media: IMedia, user: User):
        pass

    @abstractmethod
    def return_media(self, media: IMedia):
        pass

    @abstractmethod
    def get_all(self) -> [IMedia]:
        pass

    @abstractmethod
    def get_all_available(self) -> [IMedia]:
        pass

    @abstractmethod
    def get_all_non_available(self) -> [IMedia]:
        pass

    @abstractmethod
    def get_all_loaned_from_user(self, user: User) -> [IMedia]:
        pass