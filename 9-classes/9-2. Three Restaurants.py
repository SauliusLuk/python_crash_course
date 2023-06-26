class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

restaurant = Restaurant('Lomai', 'Lithuanian')
print(f"I'd like to go to the restaurant {restaurant.name}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2= Restaurant("Peledine", "American")
print(f"\nI'd like to go to {restaurant2.name}")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Hakkasan", "Asian")
print(f"\nI'd like to visit {restaurant3.name}")
restaurant3.describe_restaurant()
restaurant2.open_restaurant()
