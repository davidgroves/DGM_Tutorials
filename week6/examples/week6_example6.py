# Week6, Example6

from PIL import Image, ImageDraw

# Load the image from disk.
myimage = Image.open("london.jpg")

# Create the drawing layer so we can draw on it.
draw = ImageDraw.Draw(myimage)

# Draw two lines
draw.line([0, 0, myimage.width, myimage.height], width=10)
draw.line([0, myimage.height, myimage.width, 0], width=10)

myimage.show()
