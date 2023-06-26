def cats_dogs(filename):

    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    cats_dogs(filename)

