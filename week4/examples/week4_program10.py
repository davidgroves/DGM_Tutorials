# Week4, Program10

a = "Hello"
b = "Hello"
c = "World"
d = "World"

print(a == b or c == d)
print(a != b or c != d)
print(a == d or b == c)

print (5 > 8 or 4 < 6)
print (3 > 9 or 5 > 7)
print (0 < 1 or 4 > 6)
print (a == c or 5 < 9)
print (a == d or d == "World")

# Tricky !
print (a == c or b == "hello")
print (int(4.7) == 4 or int(5.6) == 6)
print (True == False or False != True)
