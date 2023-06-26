favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

people = ['saul', 'valma', 'jen', 'sarah', 'john']

for person in people:
    if person in favourite_languages:
        print(f'{person}, thank you for taking the poll')
    else:
        print(f"{person}, what's your favourite programming language?")