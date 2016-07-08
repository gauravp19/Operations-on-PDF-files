from PIL import Image
import os
from wand.image import Image as IMG

directory = "C:\Users\gpatil\Desktop\sasa"
os.chdir(directory)
for images in os.listdir(directory):
    name, ext = os.path.splitext(images)
    if ext == ".png":
        with Image.open(images) as image:
            image.save(name + ".pdf", "PDF", quality=100.0, resolution=100.0)



# Converting first page into JPG
with IMG(filename="2016-07-08_14-30-16.pdf[0]") as img:
     img.save(filename="temp.jpg")
# Resizing this image
with IMG(filename="/temp.jpg") as img:
     img.resize(2560, 1978)
     img.save(filename="/thumbnail_resize.jpg")