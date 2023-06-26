class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print(f"Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"this user has no special privileges")


admin = Admin('saul', 'luk')
admin.privileges.show_privileges()
admin_privileges = ["can add post", "can delete post", "can ban users"]
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()

# user1 = User('Valma', 'Joc')
# user1.increment_login_attempts()
# print(f"user {user1.first_name} has attempted to log in {user1.login_attempts} times")
# user1.increment_login_attempts()
# print(f"user {user1.first_name} has attempted to log in {user1.login_attempts} times")
# user1.increment_login_attempts()
# print(f"user {user1.first_name} has attempted to log in {user1.login_attempts} times")
# user1.reset_login_attempts()
# print(f"user {user1.first_name} has attempted to log in {user1.login_attempts} times")