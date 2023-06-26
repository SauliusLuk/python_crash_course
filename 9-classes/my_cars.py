from car import Car
from electric_car import ElectricCar

my_vw = Car('vw', 'golf', 2019)
print(my_vw.get_descriptive_name())


my_etron = ElectricCar('audi', 'e-tron', 2020)
print(my_etron.get_descriptive_name())