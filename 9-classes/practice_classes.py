class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 0


    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open")

    def set_numbers_served(self):
        print(f"{self.name} served {self.numbers_served} people tonight")

    def increment_numbers_served(self, numbers):
        self.numbers_served += numbers






restraurant = Restaurant('Dera', "African")

restraurant.describe_restaurant()
restraurant.open_restaurant()
restraurant.numbers_served = 9
restraurant.set_numbers_served()
restraurant.increment_numbers_served(9)
restraurant.set_numbers_served()