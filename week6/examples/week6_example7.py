# Week6, Example7

from PIL import Image, ImageDraw, ImageFont

# Load the image.
myimage = Image.open("london.jpg")

# Load a font (The arial font from Windows)
myfont = ImageFont.truetype("arial.ttf", size=24)

# Get a drawing layer to draw on London
dl = ImageDraw.Draw(myimage)

# Draw text in the bottom left.
dl.text((10, myimage.height - 50), "London, England",
        font=myfont)

# Show the image
myimage.show()
