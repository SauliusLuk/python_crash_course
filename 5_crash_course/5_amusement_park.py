age = int(input("Enter your age: "))

if age < 4:
    print("Your admission costs 0$")
elif age < 18:
    print("Your admission is 25$")
else:
    print("Your admission is 40$")

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price: 40
elif age >= 65:
    price = 20
print(f"Your admission cost is {price}$")

