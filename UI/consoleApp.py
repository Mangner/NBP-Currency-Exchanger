from DTOs.exchangeRate import ExchangeRate
from DTOs.exchangeRateTable import ExchangeRateTable
from Interfaces.iuserInterface import IUserInterface    
from Interfaces.iexchangeRateProvider import IExchangeRateProvider
from Interfaces.icurrencyConverter import ICurrencyConverter


class ConsoleApp(IUserInterface):

    def __init__(self, provider: IExchangeRateProvider, converter: ICurrencyConverter) ->None:
        self._provider = provider
        self._converter = converter

    
    def run(self):
        print("Pobieranie danych z NBP...")
        try:
            table = self._provider.get_exchange_rate_table()
        except Exception as e:
            print(f"Błąd pobierania danych: {e}")
            return

        print(f"Tabela nr: {table.no} z dnia: {table.effectiveDate}")


        while True:
            print("\n--- KALKULATOR WALUT ---")
            amount_str = input("Podaj kwotę (lub 'q' aby wyjść): ")
            if amount_str.lower() == 'q':
                break

            try:
                amount = float(amount_str)
            except ValueError:
                print("Błędna kwota!")
                continue

            source_code = input("Kod waluty źródłowej (np. USD, PLN): ").upper()
            target_code = input("Kod waluty docelowej (np. EUR, PLN): ").upper()

            source_rate = self._find_rate(table, source_code)
            target_rate = self._find_rate(table, target_code)

            if source_rate and target_rate:
                result = self._converter.convert(amount, source_rate, target_rate)
                print(f"{amount} {source_code} = {result:.2f} {target_code}")
            else:
                print("Nie znaleziono podanej waluty w tabeli NBP.")


    def _find_rate(self, table: ExchangeRateTable, code: str) -> ExchangeRate:
        if code == "PLN":
            return ExchangeRate("Złoty", "PLN", 1.0)
        return table.getRateByCode(code)
        