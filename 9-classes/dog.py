class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")

my_dog = Dog('Snaige', 2)
print(f"My dog's name is {my_dog.name}")
print(f"My dog {my_dog.name} is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Juode', 5)
print(f"Valmantes dog's name is {your_dog.name}")
print(f"{your_dog.name} is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()
