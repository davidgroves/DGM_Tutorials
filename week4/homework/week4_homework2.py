# Week4, Homework2

i = 1
numbers = []
while i <= 10:
    numbers.append(i)
    i = i + 1

print("The numbers")
print(numbers)
print("The numbers backwards")
print(numbers[::-1])
print("Odd numbers")
print(numbers[::2])
print("Even numbers")
print(numbers[1::2])
print("Odd numbers backwards")
print(numbers[-2::-2])
print("Even numbers backwards")
print(numbers[::-2])
