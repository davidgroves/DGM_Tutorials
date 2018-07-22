# Week4, Program4

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("This is a list with every other element in the list")
print(alphabet[::2])

print("What do these do ?")
print(alphabet[::3])
print(alphabet[1::2])
print(alphabet[:6:2])
print(alphabet[2:7:2])
print(alphabet[1:8:3])

alphabet.extend(['i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r'])
alphabet.extend(['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

print(alphabet[::2])
print(alphabet[::3])
print(alphabet[::6])
print(alphabet[13:18:2])
print(alphabet[4:20:3])
