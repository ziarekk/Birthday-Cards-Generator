from PySide2.QtGui import QPixmap
from PIL import Image, ImageQt
from PIL import ImageDraw, ImageFont

from dictionaries import backgroundImages, Wishes

import requests
import random


urlBasic = 'https://api.genderize.io?name={personName}'


def getBackground(gender):
    item = 'buffer'
    itemGender = backgroundImages[item]['gender']
    while itemGender != gender and itemGender != 'unisex':
        item = random.choice(list(backgroundImages))
        itemGender = backgroundImages[item]['gender']

    return item


def getWishes(gender):
    wishes = 'buffer'
    wishesStyle = Wishes[wishes]['gender']
    while wishesStyle != gender and wishesStyle != 'unisex':
        wishes = random.choice(list(Wishes))
        wishesStyle = Wishes[wishes]['gender']

    return wishes


def setBaseImage(base, wishes):
    with Image.open("Background_imgs/text_block.png") as text_block:
        base = Image.alpha_composite(base, text_block)
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    fnt_src = Wishes[wishes]['fnt_src']
    fnt_size = Wishes[wishes]['fnt_size']
    font = ImageFont.truetype(fnt_src, fnt_size)
    return base, txt, font


def drawText(person, base, wishes, imgBase):
    base, txt, font = setBaseImage(base, wishes)
    pilImage = Image.alpha_composite(base, txt)
    draw = ImageDraw.Draw(txt)
    fntColor = backgroundImages[imgBase]['fill']

    text1 = f'Hey {person.name()}!'
    wishesText = Wishes[wishes]['text']

    draw.text((400, 300), text1, font=font, fill=fntColor)
    draw.text((400, 345), wishesText, font=font, fill=fntColor)
    pilImage = Image.alpha_composite(base, txt)

    return pilImage


def imageConversion(person, base, wishes, imgBase):
    pilImage = drawText(person, base, wishes, imgBase)
    qtImage = ImageQt.ImageQt(pilImage)
    qtPixmap = QPixmap.fromImage(qtImage)
    return (pilImage, qtPixmap)


def generate_Card(person):
    imgBase = getBackground(person.gender())
    source = backgroundImages[imgBase]['source']
    wishes = getWishes(person.gender())

    with Image.open(source).convert("RGBA") as base:

        pilImage, qtPixmap = imageConversion(person, base, wishes, imgBase)

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
