# Week6, Program3

from PIL import Image

myimage = Image.open("london.jpg")
flipped_image = myimage.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.show()
