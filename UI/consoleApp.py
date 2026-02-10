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
        print("Fetching data from NBP...")
        try:
            table = self._provider.get_exchange_rate_table()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return

        print(f"Table no.: {table.no} from date: {table.effectiveDate}")


        while True:
            print("\n--- CURRENCY CALCULATOR ---")
            amount_str = input("Enter amount (or 'q' to quit): ")
            if amount_str.lower() == 'q':
                break

            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount!")
                continue

            source_code = input("Source currency code (e.g. USD, PLN): ").upper()
            target_code = input("Target currency code (e.g. EUR, PLN): ").upper()

            source_rate = self._find_rate(table, source_code)
            target_rate = self._find_rate(table, target_code)

            if source_rate and target_rate:
                result = self._converter.convert(amount, source_rate, target_rate)
                print(f"{amount} {source_code} = {result:.2f} {target_code}")
            else:
                print("Currency not found in the NBP table.")


    def _find_rate(self, table: ExchangeRateTable, code: str) -> ExchangeRate:
        if code == "PLN":
            return ExchangeRate("Złoty", "PLN", 1.0)
        return table.getRateByCode(code)
        