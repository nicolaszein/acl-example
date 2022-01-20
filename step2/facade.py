from .fipe_api import FipeApi


class Facade:
    def __init__(self, fipe_api=FipeApi()):
        self.__fipe_api: FipeApi = fipe_api

    def get_car_extra_info(self, car):
        marca_id = self.__get_marca_id(car.brand)
        modelo_id = self.__get_modelo_id(marca_id, car.model)
        ano_id = self.__get_anos(marca_id, modelo_id, car.year)

        return self.__fipe_api.get_infos(marca_id, modelo_id, ano_id)

    def __get_marca_id(self, brand):
        marcas = self.__fipe_api.get_marcas()

        for marca in marcas:
            if marca['nome'] == brand:
                return marca['codigo']

        return None

    def __get_modelo_id(self, marca_id, model):
        modelos = self.__fipe_api.get_modelos(marca_id=marca_id)

        for modelo in modelos:
            if modelo['nome'] == model:
                return modelo['codigo']

        return None

    def __get_anos(self, marca_id, modelo_id, year):
        anos = self.__fipe_api.get_anos(marca_id=marca_id, modelo_id=modelo_id)

        for ano in anos:
            if str(year) in ano['codigo']:
                return ano['codigo']

        return None
