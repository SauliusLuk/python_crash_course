# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}\n")
#
# describe_pet("cat", "zela")
# describe_pet('cat', 'pazuzas')
# describe_pet(animal_type='dog',pet_name='snaige')

def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}\n")

describe_pet('snaige')
describe_pet('zela', 'cat')