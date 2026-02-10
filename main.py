from Services.nbpExchangeRateProvider import NbpExchangeRateProvider
from Repositories.nbpRepository import NbpRepository
from config import URL
from Parsers.jsonParser import JsonParser
from Services.currencyConverter import CurrencyConverter


def main():
    provider = NbpExchangeRateProvider(NbpRepository(URL), JsonParser())
    exchangeRateTable = provider.get_exchange_rate_table()

    usd = exchangeRateTable.getRateByCode("USD")
    euro = exchangeRateTable.getRateByCode("EUR")

    converter = CurrencyConverter()
    result = converter.convert(50, usd, euro)
    
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()