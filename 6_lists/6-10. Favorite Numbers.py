favourite_numbers = {
    'valma': [7, 9],
    'jurga': [9,3],
    'minde': [8,4],
    'vytas': [2,1],
    'saulius': [1,]
    }

for name, numbers in favourite_numbers.items():
    print(f"{name}'s favourite numbers are:")
    for number in numbers:
        print(number)