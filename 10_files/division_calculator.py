print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFIrst number")
    if first_number == 'q':
        break
    second_number = input("\n Second number")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Division by 0 is not allowed')
    else:
        print(answer)