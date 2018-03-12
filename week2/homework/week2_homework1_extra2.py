# Week2, Homework1 Extra2

firstname = input("What is your First Name ?: ")
surname = input("What is your Surname ?: ")

my_firstname = "Dave"
my_surname = "Groves"

# Both names match.
if firstname == my_firstname and surname == my_surname:
    print("Are you me ?. We have the exact same name !")

if firstname == my_firstname and surname != my_surname:
    print("We have the same first name, but different surnames")

if firstname != my_firstname and surname == my_surname:
    print("We have the same surname, but different firstnames")

if firstname != my_firstname and surname != my_surname:
    print("We have totally different names")
