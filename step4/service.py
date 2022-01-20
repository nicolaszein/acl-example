from .domain import Car
from .facade import Facade


class Service:

    def __init__(self, facade=Facade()):
        self.__facade: Facade = facade

    def get_car_extra_info(self, car: Car):
        extra_info = self.__facade.get_car_extra_info(car)

        print(f'4 - Valor do carro: {extra_info.value} | Combustível: {extra_info.fuel_type.value}')
