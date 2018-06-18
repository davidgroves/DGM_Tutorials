# Week8, Example4

# Define a class
class Person():
    def __init__(self, firstname, surname, age):
        self.firstname = firstname
        self.surname = surname
        self.age = age

    def can_play_little_league(self):
        if self.age < 13:
            print(f"{self.firstname} {self.surname} can play little league")
        else:
            print(f"{self.firstname} {self.surname} is too old for little league")

# Define an instance of the person class
danny = Person("Danny", "Almonte", 12)

# Show if they can play little league.
danny.can_play_little_league()

# Update Danny's age.
danny.age = 14

# Show if they can play little league again.
danny.can_play_little_league()
