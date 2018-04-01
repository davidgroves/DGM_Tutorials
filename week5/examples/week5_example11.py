# Week5, Example11

yourfile = open("helloworld.txt", "r")
# Read each line into a list (with newline characters).
contents = yourfile.readlines()
print(contents)
yourfile.close()

yourfile = open("helloworld.txt", "r")
# Read each line into a list.
contents = yourfile.read().splitlines()
print(contents)
yourfile.close()

yourfile = open("helloworld.txt", "r")
# Read each line, one at a time using a for loop.
for line in yourfile:
    # rstrip removes the extra newline.
    print(line.rstrip())
yourfile.close()
