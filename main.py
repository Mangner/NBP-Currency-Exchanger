from nbpRepository import NbpRepository
from config import URL
from jsonParser import JsonParser

repo = NbpRepository(URL)
parser = JsonParser()

response = repo.get()
exchangeRatesTable = parser.parse(response)
print(exchangeRatesTable.getRateByCode("USD"))
