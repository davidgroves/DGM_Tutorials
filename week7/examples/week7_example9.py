# Week7, Example9

def maths(a, b, operator="+"):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b

print(maths(3,3,"+"))
print(maths(4,6))
print(maths(6,3,"*"))
print(maths(16,4,"/"))
print(maths(128,128))
