from car import Car
class Battery:
    def __init__(self, battery_size = 100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 250
        elif self.battery_size == 100:
            range = 300

        print(f"This car can travel about {range} miles on full charge")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"This car doesnt need gas")



my_etron = ElectricCar('audi', 'e-tron', 2020)
print(my_etron.get_descriptive_name())
my_etron.battery.describe_battery()
my_etron.fill_gas_tank()
my_etron.battery.get_range()

# my_used_car = Car('bmw', 116, 2018)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

