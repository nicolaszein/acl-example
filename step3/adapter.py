from .fipe_api import FipeApi


class Adapter:
    def __init__(self, fipe_api=FipeApi()):
        self.__fipe_api: FipeApi = fipe_api

    def get_brand_id(self, brand):
        marcas = self.__fipe_api.get_marcas()

        for marca in marcas:
            if marca['nome'] == brand:
                return marca['codigo']

        return None

    def get_model_id(self, brand_id, model):
        modelos = self.__fipe_api.get_modelos(marca_id=brand_id)

        for modelo in modelos:
            if modelo['nome'] == model:
                return modelo['codigo']

        return None

    def get_year_id(self, brand_id, model_id, year):
        anos = self.__fipe_api.get_anos(marca_id=brand_id, modelo_id=model_id)

        for ano in anos:
            if str(year) in ano['codigo']:
                return ano['codigo']

        return None

    def get_infos(self, brand_id, model_id, year_id):
        return self.__fipe_api.get_infos(brand_id, model_id, year_id)
