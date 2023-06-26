filename = 'learning_python.txt'

# with open(filename) as file_object:
#     contents = file_object.read()
#     print(f"{contents.rstrip()}\n")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Basics', 'Python Basics'))

print(f"\n")

# python_topics = ''
# for line in lines:
#     python_topics += f"{line.strip()} \n"
# print(python_topics)

