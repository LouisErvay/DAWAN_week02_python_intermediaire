from abc import ABC, abstractmethod

class IMedia(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name) -> None:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass

    @abstractmethod
    def set_author(self, author) -> None:
        pass

    @abstractmethod
    def get_status(self) -> bool:
        pass

    @abstractmethod
    def set_status(self, status) -> None:
        pass