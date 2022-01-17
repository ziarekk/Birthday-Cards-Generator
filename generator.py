from PySide2.QtGui import QPixmap
from PIL import Image, ImageQt
from PIL import ImageDraw, ImageFont

from constants import Frames, backgroundImages, Wishes
from constants import mainFont, fntSrc
from constants import urlBasic

import requests
import random


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


def getFrame(gender):
    frame = 'buffer'
    frameStyle = Frames[frame]['gender']
    while frameStyle != gender and frameStyle != 'unisex':
        frame = random.choice(list(Frames))
        frameStyle = Frames[frame]['gender']

    return frame


def setBaseImage(person, base, wishes):
    frame = getFrame(person.gender())
    with Image.open(Frames[frame]['source']) as frame_block:
        base = Image.alpha_composite(base, frame_block)
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    fntSize = Wishes[wishes]['fntSize']
    font = ImageFont.truetype(fntSrc, fntSize)
    return base, txt, font


def drawText2(txt, wishes, font):
    draw = ImageDraw.Draw(txt)
    text = Wishes[wishes]['text']
    boundingBox = [150, 150, 1050, 1050]
    shadowFont = Wishes[wishes]['shadowColor']
    x1, y1, x2, y2 = boundingBox
    w, h = draw.textsize(text, font=font)
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    draw.text((x-4, y-4), text, align='center', font=font, fill=shadowFont)
    draw.text((x, y), text, align='center', font=font, fill=mainFont)

    return txt


def combineImage(person, base, wishes, imgBase):
    base, txt, font = setBaseImage(person, base, wishes)
    pilImage = Image.alpha_composite(base, txt)

    txt = drawText2(txt, wishes, font)
    pilImage = Image.alpha_composite(base, txt)

    return pilImage


def imageConversion(person, base, wishes, imgBase):
    pilImage = combineImage(person, base, wishes, imgBase)
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
