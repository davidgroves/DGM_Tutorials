# Week6, Homework2

from PIL import Image, ImageDraw, ImageFont
import random

# Make an image, that is 2 colours only (the "1")
# and is 500x500 pixels.
image = Image.new("1", (500,500), color=1)

# Make a drawing layer so we can draw on the image
draw = ImageDraw.Draw(image)

a = [0,0]          # The top left of our triangle
b = [250,500]      # The middle bottom of our triangle
c = [500,0]        # The top right of our triangle

# Draw the outline
draw.line(a + b)
draw.line(a + c)
draw.line(b + c)

# Select a random starting point that is inside the triangle.
# Not the best method, but it does work. We pick a random point, then check if it is in the triangle.
# If so, we use it. If not, we try again until we find one that is.
point = [0,0]
while point == [0,0]:
    # Allocate a r
    prospective_point = [random.randint(0,500), random.randint(0,500)]

    # Are we in the left half of the triangle ?
    if prospective_point[0] <= 250:
        # Then check if we are inside the triangle.
        if prospective_point[1] < prospective_point[0]:
            point = prospective_point
    # Are we in the right half of the triangle
    if prospective_point[0] >= 250:
        if prospective_point[1] > prospective_point[0]:
            point = prospective_point

# We will repeat this 1 million times.

i = 0
while i < 1000000:
    # Draw a dot at the current position
    draw.point(point)
    image.show()

    # Decide if we will move towards a, b or c
    target = random.choice([a, b, c])

    # Update point to be half way between our current position,
    # and the corner of the triangle we picked.
    newx = (point[0] + target[0]) / 2
    newy = (point[1] + target[1]) / 2
    point = [newx, newy]

    # Add one to our loop counter
    i = i + 1

# Show the image.
image.show()
