from abc import ABC, abstractmethod
from DTOs.exchangeRateTable import ExchangeRateTable

class IExchangeRateProvider(ABC):

    @abstractmethod
    def get_exchange_rate_table(self) -> ExchangeRateTable:
        pass
