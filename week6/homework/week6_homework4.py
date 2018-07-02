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

i = 0
while i < 50000:
    draw.point(point)

    target = random.choice([a, b, c])

    newx = (point[0] + target[0]) / 2
    newy = (point[1] + target[1]) / 2
    point = [newx, newy]

    if i % 1000 == 0:
        image.save(f"image{i}.png")

    i = i + 1
