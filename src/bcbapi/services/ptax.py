from datetime import date
from bcbapi.config import Config
from bcbapi import PTAX
from bcbapi.parsers.ptax import ptax_parser
from bcbapi.services.base import BaseService

class PTAXService(BaseService):
    """ PTAX Service """

    def __init__(self) -> None:
        super().__init__("PTAX", ptax_parser)

    def get_ptax_rate(self, ref_date: date) -> PTAX:
        """
        Get the PTAX rate for a given date.

        Args:
            ref_date (date): the reference date to get the PTAX rate.

        Returns:
            PTAX: the PTAX rate for the given date.
        """
        endpoint = ("CotacaoDolarDia"
                    "(dataCotacao=@dataCotacao)")
        params = {
            "@dataCotacao": ref_date.strftime(Config.REQUEST_DATE_FORMAT),
            "top": 1
        }
        result = self._get(endpoint, params)
        return result[0] if result else None

    def get_daily_ptax_rate_by_period(self,
                                      start_date: date,
                                      end_date: date) -> list[PTAX]:
        """
        Get the daily PTAX rate for a given period.

        Args:
            start_date (date): the start date of the period.
            end_date (date): the end date of the period.

        Returns:
            list[PTAX]: the PTAX rate for the given period.
        """
        endpoint = ("CotacaoDolarPeriodo"
                    "(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)")
        params = {
            "@dataInicial": start_date.strftime(Config.REQUEST_DATE_FORMAT),
            "@dataFinalCotacao": end_date.strftime(Config.REQUEST_DATE_FORMAT),
            "top": (end_date - start_date).days + 1
        }
        return self._get(endpoint, params)
