from datetime import date, datetime
from bcbapi._api_client import _APIClient
from bcbapi.config import API_BASE_URL, REQUEST_DATE_FORMAT
from bcbapi import PTAX

class PTAXService:

    def __init__(self) -> None:
        self.client = _APIClient(base_url=API_BASE_URL.format(service="PTAX"))

    def __get_ptax(self, endpoint:str, params:dict) -> list[PTAX]:
        response = self.client.get(endpoint, params)

        return [
            PTAX
            (
                timestamp = datetime.strptime(value["dataHoraCotacao"], 
                                              "%Y-%m-%d %H:%M:%S.%f"),
                buy = value["cotacaoCompra"],
                sell = value["cotacaoVenda"]
            )
            for value in response
        ]

    def get_ptax_rate(self, ref_date: date) -> PTAX:
        """Get the PTAX rate for a given date.

        Args:
            ref_date (date): the reference date to get the PTAX rate.

        Returns:
            PTAX: the PTAX rate for the given date.
        """
        endpoint = "CotacaoDolarDia(dataCotacao=@dataCotacao)"
        params = {
            "@dataCotacao": ref_date.strftime(REQUEST_DATE_FORMAT),
            "top": 1
        }
        result = self.__get_ptax(endpoint, params)
        return result[0] if result else None

    def get_daily_ptax_rate_by_period(self, start_date: date, end_date: date) -> list[PTAX]:
        """Get the daily PTAX rate for a given period.

        Args:
            start_date (date): the start date of the period.
            end_date (date): the end date of the period.

        Returns:
            list[PTAX]: the PTAX rate for the given period.
        """
        endpoint = "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        params = {
            "@dataInicial": start_date.strftime(REQUEST_DATE_FORMAT),
            "@dataFinalCotacao": end_date.strftime(REQUEST_DATE_FORMAT),
            "top": (end_date - start_date).days + 1
        }
        return self.__get_ptax(endpoint, params)
