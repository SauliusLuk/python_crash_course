from car import ElectricCar

my_etron = ElectricCar('audi', 'etron', 2020)

print(my_etron.get_descriptive_name())
my_etron.battery.describe_battery()
my_etron.battery.get_range()