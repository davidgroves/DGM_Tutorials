# Week5, Homework1

import random

i = 1
while i <= 20:
    print(random.randint(1,20))
    i = i + 1

i = 1
countries = ["England", "Scotland", "Wales", "Northern Ireland"]
while i <= 20:
    print(random.choice(countries))
    i = i + 1
