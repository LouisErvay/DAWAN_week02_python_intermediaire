from abc import abstractmethod
from observers.ISubject import ISubject

class IMedia(ISubject):
    
    @abstractmethod
    def get_title(self):
        pass
    
    @abstractmethod
    def get_author(self):
        pass
    
    @abstractmethod
    def get_media_type(self):
        pass
    
    @abstractmethod
    def is_available(self):
        pass
    
    @abstractmethod
    def set_available(self, available):
        pass