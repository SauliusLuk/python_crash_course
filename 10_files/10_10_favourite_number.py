import json

filename = 'favourite_number.json'


try:
    with open(filename, 'r') as f:
        number = json.load(f)
        if number:
            print(f"Your favourtie number is {number}")
except FileNotFoundError:
    fav_number = input("What's your favourite number?")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
