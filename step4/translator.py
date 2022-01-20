from dataclasses import dataclass
import enum


class FuelType(enum.Enum):
    GASOLINE = 'GASOLINE'
    UNKNOWN = 'UNKNOWN'


@dataclass
class CarExtraInfo:
    value: float
    fuel_type: FuelType


class Translator:

    @staticmethod
    def execute(extra_info):
        value = extra_info['Valor'].replace('R$ ', '').replace('.', '').replace(',', '.')
        fuel_type = FuelType.GASOLINE if extra_info['Combustivel'] == 'Gasolina' else FuelType.UNKNOWN
        return CarExtraInfo(value=value, fuel_type=fuel_type)
