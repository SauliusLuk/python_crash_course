# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
#     print(f"Great trick, {magician}\n")
#
# print(f"thank you everyone")

# for value in range(1,5):
#     print(value)
#
# numbers = list(range(1,9))
# print(numbers)
#
# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
#
# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# for value in range(1,21):
#     print(value)
#
# million = list(range(1,10000001))
# print(max(million))
# print(min(million))
# print(sum(million))

# odd_numbers = range(1,20,2)
# for odd_number in odd_numbers:
#     print(odd_number)

# print(value * 3 for value in list(range(3,30)))
# threes = [value for value in range(3,30, 3)]
# print(threes)

# threes = list(range(3,30,3))
# for three in threes:
#     print(three)

# cubes = list(range(1,10))
# for cube in cubes:
#     print(cube ** 3)

# cubes = [ cube ** 3 for cube in range(1,10)]
# print(cubes)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:3])
# print(players[:4])
# print(players[2:])
# print(players[-3:])
# print(f"\nThere are three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('apple')
# friend_foods.append('ice cream')
#
# print(my_foods)
# print(friend_foods)

# 4-10
# my_foods = ['pizza', 'falafel', 'carrot cake']
# print(f"the first three items on the list are {my_foods[:2]}")
# print(f"The items in the middle are {my_foods[1:2]}")
# print(f"The last item is {my_foods[2:]}")

# 4-11
# pizzas = ['pepperoni', 'mozzarella', 'hawaiian', 'four cheese']
# friends_pizzas = pizzas[:]
# pizzas.append('diavola')
# friends_pizzas.append('chicken')
# print(f"my favourite pizzas are:")
# for pizza in pizzas:
#     print(pizza)
#
# print(f"my friends favourite pizzas are:")
# for pizza in friends_pizzas:
#     print(pizza)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
friends_foods.append('ice cream')
for food in my_foods:
    print(food)
print(f"my friends favourite foods are:")
for food in friends_foods:
    print(food)