class User:

    def __init__(self, first_name, last_name, username):
        self.f_name = first_name
        self.l_name = last_name
        self.username = username
        self.login_attempts = 0
        self.privileges = Privileges(['can read'])


    def describe_user(self):
        user_info = f"User details: {self.f_name}, {self.l_name}, {self.username}"
        print(user_info)


    def greet_user(self):
        print(f"Hello, {self.f_name}")


    def increment_login_attempts(self):
        print(f"You had {self.login_attempts} previous login attempts")
        self.login_attempts += 1
        print(f"You now have {self.login_attempts} login attempts")

    def reset_login_attempts(self):
        ask_for_reset = input(f"Would you like to reset your login attempts? y/n: ")
        if ask_for_reset == "y":
            self.login_attempts = 0
            print(f"Your login attempts have been reset to {self.login_attempts}")
        else:
            print(f"Your login attempts have not been reset. Number of login attempts is: {self.login_attempts}")

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"The user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])




admin = Admin("Saul", "Luk", "SaulLuk")
admin.privileges.show_privileges()
user = User("Val", 'Joc', "Vajoc")
user.privileges.show_privileges()

