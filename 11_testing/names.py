from name_function import get_formatted_name

print("Enter q any time you want to quit")
while True:
    first = input("Enter your name: ")
    if first == 'q':
        break
    last = input("Please enter your surname: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}")