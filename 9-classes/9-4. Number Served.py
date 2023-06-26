class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.numbers_served = 0


    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

    def set_numbers_served(self, numbers_served):
        self.numbers_served = numbers_served

    def increment_numbers_served(self, people):
        self.numbers_served += people

restaurant = Restaurant('Lomai', 'Lithuanian')
print(f"I'd like to go to the restaurant {restaurant.name}. It has served {restaurant.numbers_served} people")
restaurant.set_numbers_served(4)
print(f"I'd like to go to the restaurant {restaurant.name}. It has served {restaurant.numbers_served} people")
restaurant.increment_numbers_served(5)
print(f"I'd like to go to the restaurant {restaurant.name}. It has served {restaurant.numbers_served} people")
restaurant.increment_numbers_served(5)
print(f"I'd like to go to the restaurant {restaurant.name}. It has served {restaurant.numbers_served} people")


