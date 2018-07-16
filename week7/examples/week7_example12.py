# Week7, Example12

import random

print(f"Rolling 2 dice with 6 sides 10 times")
results = []
for i in range(10):
    results.append(random.randint(1,6) + random.randint(1,6))
print(results)

print(f"Rolling 3 dice with 4 sides 10 times")
results = []
for i in range(10):
    results.append(random.randint(1,4) + random.randint(1,4) + random.randint(1,4))
print(results)

print(f"Rolling 1 die with 20 sides 5 times")
results = []
for i in range(5):
    results.append(random.randint(1,20))
print(results)
