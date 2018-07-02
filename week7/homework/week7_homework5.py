# Week7, Homework5

def uk_to_int(number):
    # Remove the leading 0's.
    stripped_string = number.lstrip("0")
    return "+44" + stripped_string

def us_to_int(number):
    return "+1" + number

def de_to_int(number):
    stripped_string = number.lstrip("0")
    return "+49" + stripped_string

print(uk_to_int("0123456789"))
print(uk_to_int("0717171717"))
print(us_to_int("5551112345"))
print(us_to_int("5559876543"))
print(de_to_int("0123456789"))
print(de_to_int("0009876543"))
