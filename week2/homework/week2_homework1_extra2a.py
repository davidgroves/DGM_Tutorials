# Week2, Homework1 Extra2

firstname = input("What is your First Name ?: ")
surname = input("What is your Surname ?: ")

my_firstname = "Dave"
my_surname = "Groves"

# Fall through method

if firstname == my_firstname:
    if surname == my_surname:
        print("We have exactly the same name !")
    else:
        print("We have the same firstname, but not the same surname")
elif surname == my_surname:
        print("We have the same surname, but not the same firstname")
else:
    print("We have totally different names")
