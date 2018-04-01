# Week7, Example14

import random

def rolls(dice, sides, times):
    results = []

    for i in range(times):
        result = 0
        for j in range(dice):
            result += random.randint(1,sides)
        results.append(result)

    return(results)

print(f"Rolling 2 dice with 6 sides 10 times")
print(rolls(2,6,10))

print(f"Rolling 3 dice with 4 sides 10 times")
print(rolls(3,4,10))

print(f"Rolling 1 die with 20 sides 5 times")
print(rolls(1,20,5))
