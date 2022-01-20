from step3.domain import Car
from step3.service import Service

car = Car(brand='Audi', model='A3 1.8 Turbo 180cv 5p Mec.', year=2001)

Service().get_car_extra_info(car=car)
