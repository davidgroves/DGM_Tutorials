# Week8, Example3

# Define a class
class Person():
    def __init__(self, firstname, surname, age):
        self.firstname = firstname
        self.surname = surname
        self.age = age

def can_play_little_league(person):
    if person.age < 13:
        print(f"{person.firstname} {person.surname} can play little league")
    else:
        print(f"{person.firstname} {person.surname} is too old for little league")

# Define an instance of the person class
danny = Person("Danny", "Almonte", 12)

# Show if they can play little league.
can_play_little_league(danny)

# Update Danny's age.
danny.age = 14

# Show if they can play little league again.
can_play_little_league(danny)
