from abc import ABC, abstractmethod
from DTOs.exchangeRate import ExchangeRate 


class ICurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount: float, srcCurr: ExchangeRate, destCurr: ExchangeRate) -> float:
        pass

    