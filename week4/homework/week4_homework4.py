# Week4, Homework4

i = 0
names = []
while i < 3:
    name = input("Enter a name: ")
    names.append(name)
    i = i + 1

if names[0] == names[1] and names[1] == names[2]:
    print("All the names are the same")

if names[0] == names[1] or names[0] == names[2] or names[1] == names[2]:
    print("Some of the names are the same")

if names[0] != names[1] and names[0] != names[2] and names[1] != names[2]:
    print("None of the names are the same")
