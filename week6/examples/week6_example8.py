# Week6, Example8

from PIL import Image, ImageDraw

# Make a new image.
# It uses Red/Green/Blue colouring.
# It is 5x5 pixels in size.
image = Image.new("RGB", (5,5))

# Make a drawing layer
draw = ImageDraw.Draw(image)

# Draw the red pixels with the list of pairs of x,y locations
draw.point([(0,0), (1,0), (2,0), (3,0)], fill=(255,0,0))
draw.point([(4,0), (4,1), (4,2), (4,3)], fill=(255,0,0))

# Draw the green pixels
draw.point([(1,1), (1,2), (1,3)], fill=(0,255,0))
draw.point([(2,1), (2,2), (2,3)], fill=(0,255,0))
draw.point([(3,1), (3,2), (3,3)], fill=(0,255,0))

# Draw the blue pixels
draw.point([(0,1), (0,2), (0,3), (0,4)], fill=(0,0,255))
draw.point([(1,4), (2,4), (3,4), (4,4)], fill=(0,0,255))

# Scale the image to be 500x500 pixels instead of 5x5.
# as otherwise it will be too small to see.
scaled_image = image.resize((500,500))
scaled_image.show()
