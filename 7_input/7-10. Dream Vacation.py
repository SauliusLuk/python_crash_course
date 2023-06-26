responses = {}
polling_active = True

while polling_active:
    name = input('What is your name?')
    question = input("If you could visit one place in the world, where would you go?")

    responses[name] = question

    repeat = input("Woul you like another person to respond? y/n")
    if repeat == 'n':
        polling_active = False

print(f"--------------Poling results ---------------")
for name, response in responses.items():
    print(f"{name} would love to visit {response}")