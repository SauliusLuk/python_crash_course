name = input('Please enter your name: ')

filename = '10_3_guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(f" the guest's name is {name}")