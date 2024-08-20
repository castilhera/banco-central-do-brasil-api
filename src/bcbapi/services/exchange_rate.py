from datetime import date, datetime
from bcbapi._api_client import _APIClient
from bcbapi.config import API_BASE_URL, REQUEST_DATE_FORMAT
from bcbapi import BulletinType, ExchangeRate

class ExchangeRateService:

    def __init__(self) -> None:
        self.client = _APIClient(
            base_url=API_BASE_URL.format(service="PTAX")
        )

    def __get_exchange_rate(self, endpoint:str, params:dict) -> list[ExchangeRate]:
        response = self.client.get(endpoint, params)

        return [
            ExchangeRate
            (
                timestamp = datetime.strptime(value["dataHoraCotacao"],
                                              "%Y-%m-%d %H:%M:%S.%f"),
                buy_parity = value["paridadeCompra"],
                sell_parity = value["paridadeVenda"],
                buy_quote = value["cotacaoCompra"],
                sell_quote = value["cotacaoVenda"],
                bulletin_type = BulletinType(value["tipoBoletim"])
            )
            for value in response
        ] or None

    def get_exchange_rate(self, currency: str, ref_date: date) -> list[ExchangeRate]:
        """Get the exchange rate for a given date.

        Args:
            ref_date (date): the reference date to get the exchange rate.

        Returns:
            list[ExchangeRate]: the exchange rates for the given date.
        """
        endpoint = "CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)"
        params = {
            "@moeda": f"'{currency}'",
            "@dataCotacao": ref_date.strftime(REQUEST_DATE_FORMAT),
        }
        return self.__get_exchange_rate(endpoint, params)

    def get_daily_exchange_rate_by_period(self,
                                          currency: str,
                                          start_date: date,
                                          end_date: date) -> list[ExchangeRate]:
        """Get the daily exchange rate for a given period.

        Args:
            start_date (date): the start date of the period.
            end_date (date): the end date of the period.

        Returns:
            list[ExchangeRate]: the exchange rates for the given period.
        """
        endpoint = "CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        params = {
            "@moeda": f"'{currency}'",
            "@dataInicial": start_date.strftime(REQUEST_DATE_FORMAT),
            "@dataFinalCotacao": end_date.strftime(REQUEST_DATE_FORMAT)
        }
        return self.__get_exchange_rate(endpoint, params)
