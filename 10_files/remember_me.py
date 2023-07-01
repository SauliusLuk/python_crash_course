import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What's your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username_check = get_stored_username()
    if username_check:
        user_check = input(f"is your username {username_check}? y/n")
        if user_check == 'y':
            print(f"Welcome back, {username_check}")
        else:
            username = get_new_username()
            print(f"New username added {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
