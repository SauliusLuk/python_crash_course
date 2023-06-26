prompt = "Please enter your age"


age = 0

while age < 60:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Price: Free entrance ")
    elif age >= 3 and age < 12:
        print("Price: 10 eur ")
    else:
        print("Price: 15 eur ")


