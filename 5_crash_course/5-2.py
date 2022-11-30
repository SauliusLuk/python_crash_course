 # 5-2. More Conditional Tests
"""5-2. More Conditional Tests: You don’t have to limit the number of tests you 
create to ten. If you want to try more comparisons, write more tests and add 
them to conditional_tests.py. Have at least one True and one False result for 
each of the following:
•	 Tests for equality and inequality with strings
•	 Tests using the lower() method
•	 Numerical tests involving equality and inequality, greater than and 
less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list"""


car = 'Bmw'
print(car == 'bmw')
print(car.lower() == 'bmw')

number = 8
print(number == 7)
print(number >= 6 )
print(number <= 5)
print(number >= 8)
print(number > 6 and number % 2 == 0)
print(number > 9 or number % 2 == 0)

numbers = [1, 2, 3, 5, 9]
number = 5
print(number in numbers)
number_2 = 7
print(number_2 not in numbers)