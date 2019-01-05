import math

# This program works in cm (normally).

def inches(my_function):
    def to_inches(*args, **kwargs):
        return my_function(*args, **kwargs) / 2.54
    return to_inches

# Uncomment this decorator to see what it does.
# @inches
def area_of_circle(radius):
    return math.pi * radius * radius

print(area_of_circle(10))
print(area_of_circle(30))