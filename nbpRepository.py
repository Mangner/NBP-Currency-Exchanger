from Interfaces.irepository import IRepository
import requests

class NbpRepository(IRepository):
    
    def __init__(self, url: str):
        self._url = url

    def get(self) -> str:
        response = requests.get(self._url)
        if response.status_code == 200:
            return response.text 
        raise Exception(f"Błąd pobierania danych: {response.status_code}")
