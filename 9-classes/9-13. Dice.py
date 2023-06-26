from random import randint
x = randint(1,6)
class Die:

    def __init__(self, sides = 6):
        self.sides = sides


    def roll_die(self):
        return randint(1,self.sides)

dice = Die()

results = []
for roll_num in range(10):
    result = dice.roll_die()
    results.append(result)
print("Results of 10 rolls with a 6 sided die:")
print(results)

dice10 = Die(sides=10)
results = []
for roll_num in range(10):
    result = dice10.roll_die()
    results.append(result)
print("Results of 10 rolls with a 10 sided die:")
print(results)

dice20 = Die(sides=20)
results = []
for roll_num in range(20):
    result = dice20.roll_die()
    results.append(result)
print("Results of 10 rolls with a 20 sided die:")
print(results)