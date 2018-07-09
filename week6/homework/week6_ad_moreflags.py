from PIL import Image, ImageDraw

# French Flag:
# RGB: (0,85,164)   (255,255,255)   (239,65,53)
french = Image.new("RGB", (300, 200))
dl = ImageDraw.Draw(french)
dl.polygon([(0, 0), (100, 0), (100, 200), (0, 200)], fill=(0, 85, 164))
dl.polygon([(100, 0), (200, 0), (200, 200), (100, 200)], fill=(255, 255, 255))
dl.polygon([(200, 0), (300, 0), (300, 200), (200, 200)], fill=(239, 65, 53))
french.show()

# German flag:
# Colours: (0,0,0)  (255,0,0)   (255,204,0)
german = Image.new("RGB", (500, 300))
gd = ImageDraw.Draw(german)
gd.polygon([(0, 0), (0, 500), (500, 100), (0, 100)], fill=(0, 0, 0))
gd.polygon([(0, 100), (500, 100), (500, 200), (0, 200)], fill=(255, 0, 0))
gd.polygon([(0, 200), (500, 200), (500, 300), (0, 300)], fill=(255, 204, 0))
german.show()

# Union Flag
# Blue(1, 33, 105), Red (200, 16, 46), White (255, 255, 255)
unionflag = Image.new("RGB", (600, 300), (1, 33, 105))
ud = ImageDraw.Draw(unionflag)
# white diagonals
ud.polygon([(0, 0), (70, 0), (600, 260), (600, 300), (530, 300), (0, 35)], fill=(255, 255, 255))
ud.polygon([(525, 0), (600, 0), (600, 35), (65, 300), (0, 300), (0, 265)], fill=(255, 255, 255))
# red diagonals
ud.polygon([(0, 0), (0, 20), (600, 300), (600, 275)], fill=(200, 16, 46))
ud.polygon([(0, 300), (45, 300), (600, 0), (545, 0)], fill=(200, 16, 46))
# white cross
ud.polygon([(250, 0), (350, 0), (350, 300), (250, 300)], fill=(255, 255, 255))
ud.polygon([(0, 100), (600, 100), (600, 200), (0, 200)], fill=(255, 255, 255))
# red cross
ud.polygon([(270, 0), (330, 0), (330, 300), (270, 300)], fill=(200, 16, 46))
ud.polygon([(0, 120), (0, 180), (600, 180), (600, 120)], fill=(200, 16, 46))
unionflag.show()
