pets = []

pet = {'name' : 'snaige', 'animal' : 'dog', 'owner' : 'saulius'}
pets.append(pet)
pet = {'name' : 'zela', 'animal' : 'cat', 'owner' : 'valma'}
pets.append(pet)
pet = {'name' : 'juode', 'animal' : 'dog', 'owner' : 'minde'}
pets.append(pet)

for pet in pets:
    print(f"\nPet info:")
    for key, value in pet.items():
        print(key, value)