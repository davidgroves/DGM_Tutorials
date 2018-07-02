# Week7, Homework2

def multiply_together(numbers):
    answer = 1
    for i in numbers:
        answer = answer * i
    return answer

print(multiply_together([3,4]))
print(multiply_together([3,4,5]))
print(multiply_together([2,3,4]))
print(multiply_together([2,2,2,2]))
