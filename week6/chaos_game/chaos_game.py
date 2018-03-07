# Chaos Game

from PIL import Image, ImageDraw
import random

image = Image.new("1", (1000,1000), color=1)
draw = ImageDraw.Draw(image)

a = (0,0)           # The top left of our triangle
b = (500,1000)      # The middle bottom of our triangle
c = (1000,0)        # The top right of our triangle

point = (500,500)   # Setup our starting point in the middle of the triangle

for i in range(1000000):
    # Draw a dot at the current position
    draw.point(point)

    # Decide if we will move towards a, b or c
    target = random.choice([a, b, c])

    # Update point to be half way between our current position,
    # and the corner of the triangle we decided.
    point = (((point[0] + target[0]) / 2), ((point[1] + target[1]) / 2))

# Draw the Image
image.show()
