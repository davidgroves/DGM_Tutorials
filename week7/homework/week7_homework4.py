# Week7, Homework5

pi = 3.14159

def circleArea(radius):
    return radius * radius * pi

for radius in [3, 5, 9, 12, 44]:
    print(f"Area of circle of radius {radius} cm is {circleArea(radius)} cm squared")
