# Week5, Homework3

import random

i = 1
file = open("dice.txt", "w")
while i <= 500:
    file.write(f"{random.randint(1,6)}\n")
    i = i + 1

file.close()
