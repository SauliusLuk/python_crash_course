class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

restaurant = Restaurant('Lomai', 'Lithuanian')
print(f"I'd like to go to the restaurant {restaurant.name}")
restaurant.describe_restaurant()
restaurant.open_restaurant()



