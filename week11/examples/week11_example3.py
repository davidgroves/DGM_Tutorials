# Week11, Example3

import datetime

class Person:
    def __init__(self, **kwargs):
        self.firstname = kwargs['firstname']
        self.surname = kwargs['surname']
        self.dob = kwargs['dob']
        self.phone = kwargs['phone']

    def __repr__(self):
        return f"{self.firstname} {self.surname} was born \
                 {self.dob}, and has phone number {self.phone}"

bruce = Person(firstname = "Bruce",
               surname = "Almighty",
               dob = datetime.date(year=1,month=12,day=25),
               phone = 5550123)

print(bruce)
