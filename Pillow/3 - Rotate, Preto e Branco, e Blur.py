from PIL import Image, ImageFilter
import os

image1 = Image.open('maya.jpg')
# image1.rotate(90).save('maya_mod.jpg')
# image1.convert(mode='L').save('maya_mod.jpg')
# image1.filter(ImageFilter.GaussianBlur(15)).save('maya_mod.jpg')