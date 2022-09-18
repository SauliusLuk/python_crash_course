# requested_toppings = []
#
# requested_toppings.append('mushrooms')
# requested_toppings.append('green peppers')
# requested_toppings.append('extra cheese')
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print(f"sorry, out of {requested_topping}.")
#     else:
#         print(f"adding {requested_topping}")
#
#
# print("finished making your pizza")


# requested_toppings = []
# requested_toppings.append('mushrooms')
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"adding {requested_topping}.")
#     print("finished making pizza")
# else:
#     print(f"are you sure you want a plain pizza?")

# available_toppings = ['mushrooms', 'olives', 'green peppers',
#  'pepperoni', 'pineapple', 'extra cheese']
#
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print('adding requested topping')
#     else:
#         print(f"sorry, we don't have {requested_topping} today")
#
# print("\nfinished making pizza")

# usernames = ['admin', 'sls', 'vlm', 'dvl', 'mdg']
#
#
# for username in usernames:
#     if username == 'admin':
#         print(f'hello, {username}')
#     else:
#         print(f"hello, {username}")


# usernames = []
#
#
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print(f'hello, {username}')
#         else:
#             print(f"hello, {username}")
# else:
#     print("we need to add users")

#
# current_users = ['admin', 'sls', 'vlm', 'dvl', 'mdg']
# new_users = ['gbp', 'usd', 'sls', 'dvl']
#
# current_users_lower = [user.lower() for user in current_users]
#
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f"sorry {new_user}, plz pick another username")


ordinal_numbers = list(range(1,10))
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")
