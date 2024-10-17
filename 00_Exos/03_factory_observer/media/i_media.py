from abc import ABC, abstractmethod

class IMedia(ABC):

    @abstractmethod
    def get_name(self):
        pass