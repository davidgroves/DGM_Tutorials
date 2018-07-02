# Week8, Example2

# Define a class
class Person():
    def __init__(self, firstname, surname, age):
        self.firstname = firstname
        self.surname = surname
        self.age = age

# Define two instances of that class
uk_pm = Person("Theresa", "May", 61)
au_pm = Person("Malcom", "Turnball", 64)

# Print the UK Prime Ministers first name
# then the Australian Prime Minsters first name
print(uk_pm.firstname)
print(au_pm.firstname)
