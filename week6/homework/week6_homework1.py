# Week6, Homework1

from PIL import Image, ImageDraw

image = Image.new("1", (500,500), color=1)

draw = ImageDraw.Draw(image)

a = [0,0]
b = [250,500]
c = [500,0]

draw.line(a + b)
draw.line(a + c)
draw.line(b + c)

image.show()
