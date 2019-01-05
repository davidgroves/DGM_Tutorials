# Week11, Example2

write_number_file = open("my_numbers_file.txt", "w")
for i in range(10):
    # Note how ugly this is.
    write_number_file.write(f"{str(i)}\n")

write_number_file.close()

read_number_file = open("my_numbers_file.txt", "r")
for i in read_number_file.readlines():
    # Note we get a string with a newline on the end
    # that we need to strip.
    print(f"{i.strip()} is of type {type(i)}")
    # And this is ugly again, casting to an int
    print(f" 2 x {i.strip()} = {2 * int(i)}")
