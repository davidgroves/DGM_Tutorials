# The atexit standard library module marks functions to run on program close.

import time
import sys
import atexit

people = []

@atexit.register
def quit():
    print("When I quit, I knew about")
    print(people)

# Loop forever !
while True:
    name = input("Enter a persons name: [Hit enter to quit] ")
    if name == "":
        sys.exit(0)
    else:
        people.append(name)