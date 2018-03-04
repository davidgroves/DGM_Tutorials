# Week3, Homework1

a = int(input("Enter the first number: "))
operator = input("Enter an operator from +,-,*,/: ")
b = int(input("Enter the second number: "))

if operator == "+":
    c = a + b

if operator == "-":
    c = a - b

if operator == "*":
    c = a * b

if operator == "/":
    c = a / b

print(f"{a} {operator} {b} = {c}")
