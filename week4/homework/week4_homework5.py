# Week4, Homework5

import random

i = 0
sevens = 0
while i < 1000000:  # Do this 1 million times.
    dice1 = random.randint(1,6)  # Roll a six sided die.
    dice2 = random.randint(1, 6) # Roll another six sided die.

    total = dice1 + dice2        # Get the total of both our dice rolls.

    #
