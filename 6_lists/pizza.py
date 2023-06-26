pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],
         }

print(f"Your ordered {pizza['crust']}-crust pizza"
      f" with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t {topping}")