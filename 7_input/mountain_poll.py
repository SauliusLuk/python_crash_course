responses = {}

polling_active = True

while polling_active:
    name = input("\n what is your name?")
    response = input(" which mountain would you like to climb some day?")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input(" would you like another person to respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")