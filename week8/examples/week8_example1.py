# Week8, Example1

# Define a class
class Person():
    def __init__(self, firstname, surname, age):
        self.firstname = firstname
        self.surname = surname
        self.age = age

# Define an instance of that class
dave = Person("David", "Groves", 38)

# Print what is stored in the firstname variable,
# of the "dave" instance of the class Person.
print(dave.firstname)
