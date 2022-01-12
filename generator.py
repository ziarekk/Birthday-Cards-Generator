from PIL import Image, ImageQt
from PIL import ImageDraw, ImageFont
from PySide2.QtGui import QPixmap

import requests
import random


urlBasic = 'https://api.genderize.io?name={personName}'

backgroundsDict = {
    'back_1': "Background_imgs/back_1.jpg",
    'back_2': "Background_imgs/back_2.jpg",
    'back_3': "Background_imgs/back_3.jpg",
    'back_4': "Background_imgs/back_4.jpg"

}


def getBackground():
    return random.choice(list(backgroundsDict))


def imageConversion(base, txt, fnt):
    pilImage = Image.alpha_composite(base, txt)
    draw = ImageDraw.Draw(txt)
    draw.text((150, 40), "Hello", font=fnt, fill=(56, 123, 12, 128))
    draw.text((150, 100), "World", font=fnt, fill=(56, 123, 12, 255))
    pilImage = Image.alpha_composite(base, txt)

    qtImage = ImageQt.ImageQt(pilImage)
    qtPixmap = QPixmap.fromImage(qtImage)
    return (pilImage, qtPixmap)


def generate_Card():
    imgBase = getBackground()
    with Image.open(backgroundsDict[imgBase]).convert("RGBA") as base:
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 80)
        pilImage, qtPixmap = imageConversion(base, txt, fnt)

    return (pilImage, qtPixmap)


class Person():
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def gender(self):
        nameInfo = requests.get(urlBasic.format(personName=self.name())).json()
        gender = nameInfo['gender']
        return gender
