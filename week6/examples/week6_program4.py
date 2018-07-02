# Week6, Program4

from PIL import Image

myimage = Image.open("london.jpg")
turned_image = myimage.rotate(180)
turned_image.show()
