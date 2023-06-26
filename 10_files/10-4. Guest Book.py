file_name = '10_4_guest_book'
print('Enter quit when finished')

while True:
    name_input = input('Please enter your name: ')

    if name_input == 'quit':
        break
    else:
        with open(file_name, 'w') as file_object:
            print(f"Welcome, {name_input}")
            file_object.write("This guest's name is {name_input}")
        print("You've been added to the guestbook")

