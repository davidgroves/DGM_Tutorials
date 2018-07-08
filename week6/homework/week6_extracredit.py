# Week6, Extra Credit

from PIL import Image, ImageDraw, ImageColor

# Make our image.
image = Image.new("RGB", (600,400))

# Make a drawing layer so we can draw on the image
draw = ImageDraw.Draw(image)

# Draw the blue part
draw.polygon([(0, 0), (0, 400), (200, 400), (200, 0)], fill=ImageColor.getrgb("Blue"))

# Draw the white part
draw.polygon([(200, 0), (200, 400), (400, 400), (400, 0)], fill=ImageColor.getrgb("White"))

# Draw the red part
draw.polygon([(400, 0), (400, 400), (600, 400), (600, 0)], fill=ImageColor.getrgb("Red"))

image.show()
