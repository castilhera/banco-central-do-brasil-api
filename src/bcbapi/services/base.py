from abc import ABC
from requests import Response
from bcbapi._api_client import _APIClient
from bcbapi.config import Config

class BaseService(ABC):

    def __init__(self, service: str, parser) -> None:
        self._client = _APIClient(
            base_url=f"https://olinda.bcb.gov.br/olinda/servico/{service}/versao/v1/odata/"
        )
        self._parser = parser

    def __set_format(self, params:dict[str,str]=None) -> dict[str,str]:
        """ Includes 'format' param to the request. """
        if not params:
            params = {}
        params["$format"] = Config.RESPONSE_FORMAT
        return params

    def __parse_response(self, response: Response):
        """ Parse the response. """
        if not response:
            return None

        data = response.json()

        if not 'value' in data:
            return None

        data_value = data['value']

        return [self._parser(obj) for obj in data_value] or None

    def _get(self, endpoint:str, params:dict[str, str]=None) -> list:
        """ Make a GET request to the API. """
        params = self.__set_format(params)
        response = self._client.get(endpoint, params)
        return self.__parse_response(response)

    def _post(self, endpoint:str, params:dict[str, str]=None) -> list:
        """ Make a POST request to the API. """
        params = self.__set_format(params)
        response = self._client.post(endpoint, params)
        return self.__parse_response(response)
