from abc import ABC, abstractmethod

class IUser(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name) -> None:
        pass