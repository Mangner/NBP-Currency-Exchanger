from abc import ABC, abstractmethod
from DTOs.exchangeRateTable import ExchangeRateTable

class IParser(ABC):
    
    @abstractmethod
    def parse(self, data: str) -> ExchangeRateTable:
        pass