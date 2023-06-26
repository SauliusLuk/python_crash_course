while True:
    try:
        no1 = input("Enter no1: ")
        if no1 == 'q':
            break
        no1 = int(no1)

        no2 = input("Enter no2: ")
        if no2 == 'q':
            break
        no2 = int(no2)
    except ValueError:
        print("Numbers only plz")
    else:
        sum = no1 + no2
        print(f"The sum on {no1} and {no2} is {sum}")
