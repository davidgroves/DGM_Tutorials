# Week6, Homework3

from PIL import Image, ImageDraw, ImageFont
import random

# Make an image, that is 2 colours only (the "1")
# and is 500x500 pixels.
image = Image.new("1", (500,500), color=1)

# Make a drawing layer so we can draw on the image
draw = ImageDraw.Draw(image)

a = [0,500]
b = [250,0]
c = [500,500]

# Draw the outline
draw.line(a + b)
draw.line(a + c)
draw.line(b + c)

# Select a random starting point.
point = [random.randint(0,500), random.randint(0,500)]

# We will repeat this 1 million times.
i = 0
while i < 10000:
    # Draw a dot at the current position
    draw.point(point)

    # Decide if we will move towards a, b or c
    target = random.choice([a, b, c])

    # Update point to be half way between our current position,
    # and the corner of the triangle we picked.
    newx = (point[0] + target[0]) / 2
    newy = (point[1] + target[1]) / 2
    point = [newx, newy]

    # Add one to our loop counter
    i = i + 1

    # Check if we want to save the image.
    if i % 500 == 0:
        image.save(f"image{i}.png")
