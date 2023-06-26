prompt = "Please select your toppings: "
prompt += "\nWhen done, quit"

while True:
    toppings = input(prompt)

    if toppings == quit:
        break
    else:
        print(f"You have selected the follwoing toppings {toppings}")
