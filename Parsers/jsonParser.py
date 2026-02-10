from Interfaces.iparser import IParser
from DTOs.exchangeRate import ExchangeRate
from DTOs.exchangeRateTable import ExchangeRateTable
import json


class JsonParser(IParser):

    def parse(self, data: str) -> ExchangeRateTable:
        data = json.loads(data)
        
        no = data[0]['no']
        effectiveDate = data[0]['effectiveDate']
        rates = data[0]['rates']
        
        parsedRates = []

        for rate in rates:
            parsedRates.append(ExchangeRate(rate['currency'], rate['code'], rate['mid']))

        return ExchangeRateTable(no, effectiveDate, parsedRates)

        