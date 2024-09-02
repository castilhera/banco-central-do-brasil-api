from bcbapi import Currency
from bcbapi.parsers.currency import currency_parser
from bcbapi.services.base import BaseService

class CurrencyService(BaseService):
    """ Currency Service """

    def __init__(self) -> None:
        super().__init__("PTAX", currency_parser)

    def get_all(self) -> list[Currency]:
        """
        Get all currencies.

        Returns:
            list[Currency]: the list of currencies.
        """
        endpoint = "Moedas"
        return self._get(endpoint)
