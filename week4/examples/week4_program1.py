# Week4, Program1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("This is method one, with a while loop.")
i = 4
output = []
while i <= 6:
    output.append(alphabet[i])
    i = i + 1
print(output)

print("=====================================")
print("This is method two, with slices.")
print(alphabet[4:7])
