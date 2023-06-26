prompt = "Please enter your age"



while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
    if age < 3:
        print("Price: Free entrance ")
    elif age >= 3 and age < 12:
        print("Price: 10 eur ")
    else:
        print("Price: 15 eur ")


