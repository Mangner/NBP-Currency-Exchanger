
class ExchangeRate:

    def __init__(self, currency: str, code: str, mid: float) -> None:
        self._currency = currency
        self._code = code
        self._mid = mid

    def __str__(self):
        return f"""
            \rCurrency: {self._currency}
            \rCode: {self._code}
            \rMid: {self._mid}
        """

    @property
    def currency(self) -> str:
        return self._currency
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def mid(self) -> float:
        return self._mid
    
    @currency.setter
    def currency(self, newCurrency: str) -> None:
        self._currency = newCurrency

    @code.setter
    def code(self, newCode: str) -> None:
        self._code = newCode

    @mid.setter
    def mid(self, newMid: float) -> None:
        if newMid < 0.:
            raise ValueError("Kurs nie może być ujemny")
        self._mid = newMid
