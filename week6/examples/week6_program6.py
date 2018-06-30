# Week6, Program6

from PIL import Image, ImageDraw

myimage = Image.open("london.jpg")

print(f"This image is {myimage.width} pixels wide")
print(f"This image is {myimage.height} pixels tall")
print(f"This image is in the {myimage.format} format")
