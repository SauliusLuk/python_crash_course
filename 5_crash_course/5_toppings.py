# requested_toppings = ['mushrooms', 'onions', 'pineapple', 'extra cheese']
#
# for topping in requested_toppings:
#     if topping == 'pineapple':
#         print('Sorry, pineapple not available')
#     else:
#         print(f"Adding {topping}")
#
# print("\n finished making your pizza")

# requested_toppings = []
#
# if requested_toppings:
#     for topping in requested_toppings:
#         print(f'Adding {requested_toppings}')
#     print("\n finished making your pizza")
# else:
#     print(f'Are you sure you want a plain pizza?')

available_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f'Sorry, we dont have {requested_topping}')

print("\n finished making your pizza")