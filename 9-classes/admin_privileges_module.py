from user_module import User
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


