from Interfaces.icurrencyConverter import ICurrencyConverter
from DTOs.exchangeRate import ExchangeRate


class CurrencyConverter(ICurrencyConverter):

    def convert(self, amount: float, srcCurr: ExchangeRate, destCurr: ExchangeRate) -> float:
        srcRate = srcCurr.mid
        destRate = destCurr.mid

        return amount * srcRate / destRate
    