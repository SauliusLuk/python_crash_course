file = 'programming_poll.txt'

print('Type "quit" any time you would like to quit')

while True:
    name = input('Please enter your favourite programming language: ')
    if name == 'quit':
        break
    else:
        with open(file, 'a') as poll_file:
            poll_file.write(f"{name} \n")
            print('Name has been added to the programming poll')
