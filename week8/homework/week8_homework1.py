# Week8, Homework1

import datetime

class Person():
    def __init__(self, firstname, surname, dob):
        self.firstname = firstname
        self.surname = surname
        self.dob = dob

james = Person(firstname = "James",
               surname = "Watson",
               dob = datetime.datetime(day=6, month=4, year=1928))

print (james.age())
