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

# Alternative
files = ['cats.txt', 'dogs.txt']

for file in files:
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read()
            print(f"Here's a content of the {file} file:\n{contents}")
    except FileNotFoundError:
        print(f"the file {file} not found")