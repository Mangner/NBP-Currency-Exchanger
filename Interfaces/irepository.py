from abc import ABC, abstractmethod


class IRepository(ABC):

    @abstractmethod
    def get(self) -> str:
        pass