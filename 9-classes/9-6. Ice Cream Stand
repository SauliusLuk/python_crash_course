class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 0


    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine} cuisine")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine ='ice_cream'):
        super().__init__(name, cuisine)
        self.flavours = []


    def show_flavours(self):
        print(f"{self.name} sells the following flavours")
        for flavour in self.flavours:
            print(f"- {flavour}")


shop = IceCreamStand('Ice Ice Baby')
shop.flavours = ['vanilla', 'chocolate', 'cherry']

shop.describe_restaurant()
shop.show_flavours()
