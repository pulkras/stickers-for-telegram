from PIL import Image, ImageOps
import glob
import os
import time
def creatingStickers(image_path):
    with Image.open(image_path) as image:
        # borderImage = ImageOps.expand(image, border=10, fill="white")
        width, height = image.size
        if height > width:
            newImage = image.resize((width, 512))
        elif width > height:
            newImage = image.resize((512, height))
        else:
            newImage = image.resize((512, 512))
        newImage.save(f"newStickers/{int(time.time())}.png")

def getSize(image_path):
    image = Image.open(image_path)
    width, height = image.size
    print(width)
    print(height)

def deleteOldImage(image_path):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), image_path)
    os.remove(path)

for image in glob.glob("oldImages/*.jpg"):
    creatingStickers(image)
    deleteOldImage(image)
    print(f"{image} - обработано")
    time.sleep(3)
