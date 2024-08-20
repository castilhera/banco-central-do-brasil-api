from bcbapi._api_client import _APIClient
from bcbapi.config import API_BASE_URL
from bcbapi import Currency, CurrencyType

class CurrencyService:

    def __init__(self) -> None:
        self.client = _APIClient(base_url=API_BASE_URL.format(service="PTAX"))

    def get_all(self) -> list[Currency]:
        """Get all currencies.

        Returns:
            list[Currency]: the list of currencies.
        """
        endpoint = "Moedas"
        response = self.client.get(endpoint)

        return [
            Currency
            (
                code = value["simbolo"],
                name = value["nomeFormatado"],
                type = CurrencyType[value["tipoMoeda"]]
            )
            for value in response
        ]
