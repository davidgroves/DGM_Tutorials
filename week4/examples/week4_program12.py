# Week4, Program12

a = "Hello"
b = "Hello"
c = "World"
d = "World"

# Using 3 and statements
print(a == b and b == a and c == d)
print(1 == 1 and 3 > 4 and c == d)
print(4 * 4 == 16 and 5 * 5 == 25 and 6 * 6 == 36)

# Using 3 or statements. Only one thing needs to be true.
print(a == c or d == a or b == c)
print(a == "Hello" or b == "World" or c == "Hello")
print(a != "Hello" or b == "World" or 4 < 6)

# Mixing and/or without brackets (not recommended !)
print(1 == 2 and 2 == 2 or 3 == 4)
print(a == b or 5 == 4 and 3 == 3)

# Mixing and/or with brackets (recommended)
print((1 == 2 and 2 == 2) or 3 == 4)
print(1 == 2 and (2 == 2 or 3 == 4))
print((a == b or 5 == 4) and 3 == 3)

# More complex examples
print((1 == 2 and 3 == 4) or (4 == 5 and 4 == 4))
print((1 == 2 and 3 == 4) or (5 == 5 and 4 == 4))
print((1 == 1 or 3 == 4) and (2 == 3 or 4 == 4))
