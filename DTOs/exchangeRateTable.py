from DTOs.exchangeRate import ExchangeRate
from typing import Optional

class ExchangeRateTable:

    def __init__(self, no: str, effectiveDate: str, rates: list[ExchangeRate]) -> None:
        self._no = no
        self._effectiveDate = effectiveDate
        self._rates = rates

    @property
    def no(self) -> str:
        return self._no

    @property
    def effectiveDate(self) -> str:
        return self._effectiveDate
    
    @property 
    def rates(self) -> list[ExchangeRate]:
        return self._rates

    @no.setter
    def no(self, newNo: str) -> None:
        self._no = newNo

    @effectiveDate.setter
    def effectiveDate(self, newEffectiveDate: str) -> None:
        self._effectiveDate = newEffectiveDate        

    @rates.setter
    def rates(self, newRates) -> None:
        self._rates = newRates

    def getRateByCode(self, code) -> Optional[ExchangeRate]:
        for rate in self._rates:
            if rate.code == code:
                return rate
        return None