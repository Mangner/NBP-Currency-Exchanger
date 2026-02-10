from Interfaces.iexchangeRateProvider import IExchangeRateProvider
from Interfaces.iparser import IParser
from Interfaces.irepository import IRepository
from DTOs.exchangeRateTable import ExchangeRateTable


class NbpExchangeRateProvider(IExchangeRateProvider):

    def __init__(self, repository: IRepository, parser: IParser):
        self._repository = repository
        self._parser = parser

    def get_exchange_rate_table(self) -> ExchangeRateTable:
        raw_data = self._repository.get()
        return self._parser.parse(raw_data)
