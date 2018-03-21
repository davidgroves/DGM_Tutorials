# Week6, Example4

from PIL import Image

myimage = Image.open("london.jpg")
greyscale_image = myimage.convert('L')
greyscale_image.show()
