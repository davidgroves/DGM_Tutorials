import random

# Pure functions have the following properties.
# - Given the same inputs, they always return the same outputs.
# - They manipulate nothing outside the function (no side effects).

# pure_add only depends on the inputs, impure_add also depends on g, which can be changed outside the function
# and calling the function with the same inputs can result in different outputs.

def pure_add(x,y):
    return x + y

g = 2
def impure_add(y):
    return g + y

print("Pure Add: ")
print(pure_add(2,2))
print(pure_add(5,2))

print("============")
print("Impure Add")
print(impure_add(2))
g = 5
print(impure_add(2))

# This is technically an impure function, as it has a side effect of writing to the screen.
# This is a bad idea, as you can't use this function anywhere else (say inside another function), because
# all it does is print things to the screen.
def print_add(x,y):
    print(x + y)

print("============")
print("Print Add")
print_add(2,2)
print_add(5,2)

# And this is also technically an impure function, as even calling it with the same arguments, it
# can return different answers. This is the kind of function I will make an exception for, as the purpose of it
# is to return randomness.

def roll_dice(dice=1, sides=6):
    total = 0
    for i in range(dice + 1):
        total += random.randint(1,sides)
    return total

print("===========")
print("roll_dice(dice=10,sides=20)")
for i in range(10):
    print(roll_dice(10,20))
