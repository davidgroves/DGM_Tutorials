# Week5, Homework5

import random

### Setup the dictionary.
results = {}            # Make an empty dictionary
i = 2
while i <= 12:          # Populate the keys 2 to 12 with values of 0
    results[i] = 0
    i = i + 1

### Simulate the 1,000,000 dice rolls.
i = 0
while i <= 1000000:
    die1 = random.randint(1,6)              # Roll a die
    die2 = random.randint(1,6)              # Roll another die
    result = die1 + die2                    # Add the results together
    results[result] = results[result] + 1   # Record the result
    i = i + 1

for total, count in results.items():
    print(f"You rolled a {total} - {count} times")
