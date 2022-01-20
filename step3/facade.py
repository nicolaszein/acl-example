from .adapter import Adapter


class Facade:
    def __init__(self, adapter=Adapter()):
        self.__adapter: Adapter = adapter

    def get_car_extra_info(self, car):
        brand_id = self.__adapter.get_brand_id(car.brand)
        model_id = self.__adapter.get_model_id(brand_id, car.model)
        year_id = self.__adapter.get_year_id(brand_id, model_id, car.year)

        return self.__adapter.get_infos(brand_id, model_id, year_id)
