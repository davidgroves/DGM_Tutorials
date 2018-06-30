# Week4, Program5

# Method1
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_backwards = []
i = 9
while i >= 0:
    numbers_backwards.append(numbers[i])
    i = i - 1

print(f"The numbers from 1 to 10 are {numbers}")
print(f"The numbers from 10 to 1 are {numbers_backwards}")

# Method2
print(f"The numbers from 1 to 10 are {numbers}")
print(f"The numbers from 10 to 1 are {numbers[::-1]}")

