# Week6, Homework1

from PIL import Image, ImageDraw

image = Image.new("1", (500,500), color=1)

draw = ImageDraw.Draw(image)

a = [100,100]
b = [400,250]
c = [100,400]

draw.line(a + b)
draw.line(a + c)
draw.line(b + c)

image.show()
