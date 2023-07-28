class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

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

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"Upgrading the car battery. This car now has {self.battery_size} kWh battery")
        else:
            print(f"Unable to upgrade the battery, the size is already 100kWh")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()