from datetime import date
from bcbapi import ExchangeRate
from bcbapi.config import Config
from bcbapi.parsers.exchange_rate import exchange_rate_parser
from bcbapi.services.base import BaseService

class ExchangeRateService(BaseService):
    """ Exchange Rate Service """

    def __init__(self) -> None:
        super().__init__("PTAX", exchange_rate_parser)

    def get_exchange_rate(self, currency: str, ref_date: date) -> list[ExchangeRate]:
        """
        Get the exchange rate for a given date.

        Args:
            ref_date (date): the reference date to get the exchange rate.

        Returns:
            list[ExchangeRate]: the exchange rates for the given date.
        """
        endpoint = ("CotacaoMoedaDia"
                    "(moeda=@moeda,dataCotacao=@dataCotacao)")
        params = {
            "@moeda": f"'{currency}'",
            "@dataCotacao": ref_date.strftime(Config.REQUEST_DATE_FORMAT),
        }
        return self._get(endpoint, params)

    def get_daily_exchange_rate_by_period(self,
                                          currency: str,
                                          start_date: date,
                                          end_date: date) -> list[ExchangeRate]:
        """
        Get the daily exchange rate for a given period.

        Args:
            start_date (date): the start date of the period.
            end_date (date): the end date of the period.

        Returns:
            list[ExchangeRate]: the exchange rates for the given period.
        """
        endpoint = ("CotacaoMoedaPeriodo"
                    "(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)")
        params = {
            "@moeda": f"'{currency}'",
            "@dataInicial": start_date.strftime(Config.REQUEST_DATE_FORMAT),
            "@dataFinalCotacao": end_date.strftime(Config.REQUEST_DATE_FORMAT)
        }
        return self._get(endpoint, params)
