# Week7, Homework5

def strip_leading_zeros(number):
    return number.lstrip("0")

def add_country_code(number, countrycode):
    return "+" + str(countrycode) + number

def uk_to_int(number):
    return add_country_code(strip_leading_zeros(number), 44)

def us_to_int(number):
    return add_country_code(number, 1)

def de_to_int(number):
    return add_country_code(strip_leading_zeros(number), 49)

print(uk_to_int("0123456789"))
print(uk_to_int("0717171717"))
print(us_to_int("5551112345"))
print(us_to_int("5559876543"))
print(de_to_int("0123456789"))
print(de_to_int("0009876543"))
