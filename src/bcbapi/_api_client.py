import requests


class _APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
    
    def __set_format(self, params:dict[str,str]=None) -> dict[str,str]:
        if not params:
            params = {}
        params["format"] = "json"
        return params
    
    def __handle_response(self, response: dict):
        if 'value' in response:
            return response['value']

    def get(self, endpoint:str, params:dict[str,str]=None):
        params = self.__set_format(params)

        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return self.__handle_response(response.json())

    def post(self, endpoint:str, params:dict[str,str]=None):
        params = self.__set_format(params)

        response = requests.post(f"{self.base_url}/{endpoint}", json=params)
        response.raise_for_status()
        return self.__handle_response(response.json())
