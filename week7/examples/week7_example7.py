# Week7, Example7

def print_seperated(items, seperator=" "):
    for i in items[:-1]:
        print (f"{i}{seperator}", end="")
    print(f"{items[-1]}")

numbers = [1,2,3,4,5]

print_seperated(numbers)
print_seperated(numbers, seperator=",")
print_seperated(numbers, seperator=", ")
print_seperated(numbers, seperator="-->")
print_seperated(numbers, seperator="\n")
