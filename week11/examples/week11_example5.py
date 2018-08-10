# Week11, Example5

import datetime

class Person:
    def __init__(self, **kwargs):
        self.firstname = kwargs['firstname']
        self.surname = kwargs['surname']
        self.dob = kwargs['dob']
        self.phone = kwargs['phone']

    def __repr__(self):
        return f"{self.firstname} {self.surname} was born {self.dob}, and has phone number {self.phone}"

    def save(self, filename):
        f = open(filename, "w")
        f.write(f"{self.firstname},{self.surname},{self.dob},{self.phone}")
        f.close()

def load_person(filename):
    f = open(filename, "r")
    # Read the text line in.
    line = f.readline()

    # Split the line on ,
    splitline = line.split(",")

    firstname = splitline[0]
    surname = splitline[1]
    # strftime takes a string and turns it into a datetime object
    # following a format spec. The next line might look a bit "magical" (sorry !)
    dob = datetime.datetime.strptime(splitline[2], "%Y-%m-%d").date()
    phone = int(splitline[3])

    return(Person(firstname = firstname,
                  surname = surname,
                  dob = dob,
                  phone = phone))


bruce = load_person("bruce.txt")
print(bruce)
