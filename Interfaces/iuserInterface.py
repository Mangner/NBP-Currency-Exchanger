from abc import ABC, abstractmethod

class IUserInterface(ABC):
    
    @abstractmethod
    def run(self):
        pass