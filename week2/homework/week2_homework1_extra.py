# Week2, Homework1 Extra

firstname = input("What is your First Name ?: ")
surname = input("What is your Surname ?: ")

if firstname == "Dave":
    print("heh, you share my first name !")

if surname == "Groves":
    print("heh, you share my surname !")

if firstname == "Dave" and surname == "Groves":
    print("You are me ! (method 1 - with and)")

if firstname == "Dave":
    if surname == "Groves":
        print("You are me ! (method 2 - nested if statements)")
