from random import choice

numbers = [1,2,'a',4,'d','c','7','8','q','v']

winning_numbers = []

print(f"Pulling winning numbers:")
while len(winning_numbers) < 4:
    lottery_number = choice(numbers)
    winning_numbers.append(lottery_number)
    print(f"you pulled {lottery_number}")

print(f"The winning number is {winning_numbers}")
