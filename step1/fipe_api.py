import requests


class FipeApi:

    def __init__(self):
        self.__host = 'https://parallelum.com.br/fipe/api/v1/carros'

    def get_marcas(self):
        url = f'{self.__host}/marcas'

        response = requests.get(url, headers=self.__default_headers())
        response.raise_for_status()

        return response.json()

    def get_modelos(self, marca_id):
        url = f'{self.__host}/marcas/{marca_id}/modelos'

        response = requests.get(url, headers=self.__default_headers())
        response.raise_for_status()

        return response.json()['modelos']

    def get_anos(self, marca_id, modelo_id):
        url = f'{self.__host}/marcas/{marca_id}/modelos/{modelo_id}/anos'

        response = requests.get(url, headers=self.__default_headers())
        response.raise_for_status()

        return response.json()

    def get_infos(self, marca_id, modelo_id, ano_id):
        url = f'{self.__host}/marcas/{marca_id}/modelos/{modelo_id}/anos/{ano_id}'

        response = requests.get(url, headers=self.__default_headers())
        response.raise_for_status()

        return response.json()

    def __default_headers(self):
        return {'User-Agent': None, 'Content-Type': 'application/json'}
