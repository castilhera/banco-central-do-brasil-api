from requests import get, post

class _APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def __set_format(self, params:dict[str,str]=None) -> dict[str,str]:
        """Includes 'format' param to the request.
        """
        if not params:
            params = {}
        params["$format"] = "json"
        return params

    def __parse_response(self, response):
        """Parse the response.
        """
        if response:
            json = response.json()
            return json['value'] if 'value' in json else None
        return None

    def get(self, endpoint:str, params:dict[str,str]=None):
        """Use a HTTP Client to GET data.
        """
        params = self.__set_format(params)

        response = get(f"{self.base_url}/{endpoint}",
                       params=params,
                       timeout=5)
        response.raise_for_status()
        return self.__parse_response(response)

    def post(self, endpoint:str, params:dict[str,str]=None):
        """Use a HTTP Client to POST data.
        """
        params = self.__set_format(params)

        response = post(f"{self.base_url}/{endpoint}",
                        json=params,
                        timeout=5)
        response.raise_for_status()
        return self.__parse_response(response)
