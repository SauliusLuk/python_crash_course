def greet_users(names):
    for name in names:
        msg = f"Hello, {name}"
        print(msg)

usernames = ['saul', 'valma', 'minde']
greet_users(usernames)