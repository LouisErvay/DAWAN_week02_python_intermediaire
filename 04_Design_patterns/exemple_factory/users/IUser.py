from abc import ABC, abstractmethod

class IUser(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_address(self):
        pass