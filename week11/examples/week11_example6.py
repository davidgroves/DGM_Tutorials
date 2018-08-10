# Week11, Example6

import datetime
import pickle

class Person:
    def __init__(self, **kwargs):
        self.firstname = kwargs['firstname']
        self.surname = kwargs['surname']
        self.dob = kwargs['dob']
        self.phone = kwargs['phone']

    def __repr__(self):
        return f"{self.firstname} {self.surname} was born {self.dob}, and has phone number {self.phone}"

bruce = Person(firstname = "Bruce",
               surname = "Almighty",
               dob = datetime.date(year=1,month=12,day=25),
               phone = 5550123)

# Save bruce to a file
output_file = open("bruce.pickle", "wb")
pickle.dump(bruce, output_file)
output_file.close()

# Load new bruce from the file
input_file = open("bruce.pickle", "rb")
new_bruce = pickle.load(input_file)
print(new_bruce)
