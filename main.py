from Services.nbpExchangeRateProvider import NbpExchangeRateProvider
from Repositories.nbpRepository import NbpRepository
from Parsers.jsonParser import JsonParser
from Services.currencyConverter import CurrencyConverter
from UI.consoleApp import ConsoleApp
from UI.guiApp import GuiApp
from config import URL


def main():
    repository = NbpRepository(URL)
    parser = JsonParser()
    provider = NbpExchangeRateProvider(repository, parser)
    converter = CurrencyConverter()

    #app = ConsoleApp(provider, converter)
    app = GuiApp(provider, converter)
    app.run()


if __name__ == "__main__":
    main()