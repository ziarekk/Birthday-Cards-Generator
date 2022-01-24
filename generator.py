from PySide2.QtGui import QPixmap
from PIL import Image, ImageQt
from PIL import ImageDraw, ImageFont

from constants import Frames, backgroundImages, Wishes
from constants import mainFont, fntSrc
from constants import urlBasic

from model_io import load_wishes

import requests
import random


def getItem(gender, dict):
    """
    Function randomly chooses item from the dictionary.
    Its choose depends on the gender of the person.
    It can be used to choose: background, frame or wishes.
    Returns choosen item. (key of the dictionary)
    """
    item = 'buffer'
    itemGender = dict[item]['gender']
    while itemGender != gender and itemGender != 'unisex':
        item = random.choice(list(dict))
        itemGender = dict[item]['gender']

    return item


def setBaseImage(person, base, wishes):
    """
    Function sets base for the bithday card.
    Function gets random frame and combines it with background.
    Creates base for the text, and gets info about the font.
    Returns: combined background, base for the text, font size and source.
    """
    frame = getItem(person.gender(), Frames)
    with Image.open(Frames[frame]['source']) as frame_block:
        base = Image.alpha_composite(base, frame_block)
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    fntSize = Wishes[wishes]['fntSize']
    font = ImageFont.truetype(fntSrc, fntSize)
    return base, txt, font


def drawText(txt, wishes, font):
    """
    Function draws wishes text in the center spot of the card.
    Returns image with text drawn on it, ready to be combined.
    """
    draw = ImageDraw.Draw(txt)
    text = load_wishes(Wishes[wishes]['text'])
    boundingBox = [150, 150, 1050, 1050]
    shadowFont = Wishes[wishes]['shadowColor']
    x1, y1, x2, y2 = boundingBox
    w, h = draw.textsize(text, font=font)
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    draw.text((x-4, y-4), text, align='center', font=font, fill=shadowFont)
    draw.text((x, y), text, align='center', font=font, fill=mainFont)

    return txt


def combineImage(person, base, wishes):
    """
    Function combines base (generated with setBaseImage function)
    and image with wishes text (generated with drawText function)
    Returns birthday card in PIL.Image format.
    """
    base, txt, font = setBaseImage(person, base, wishes)
    txt = drawText(txt, wishes, font)
    pilImage = Image.alpha_composite(base, txt)

    return pilImage


def imageConversion(pilImage):
    """
    Function converts PIL.Image to QPixamp
    """
    qtImage = ImageQt.ImageQt(pilImage)
    qtPixmap = QPixmap.fromImage(qtImage)
    return qtPixmap


def generate_Card(person):
    """
    Function generates Birthday Card.
    Retruns it as PIL.Image and QPixamp
    """
    imgBase = getItem(person.gender(), backgroundImages)
    source = backgroundImages[imgBase]['source']
    wishes = getItem(person.gender(), Wishes)

    with Image.open(source).convert("RGBA") as base:
        pilImage = combineImage(person, base, wishes)
        qtPixmap = imageConversion(pilImage)

    return (pilImage, qtPixmap)


class Person():
    """
    Class Person,
    variable - name (str)
    method name: returns name of the person
    method gender: returns assumed gender of the person
    """
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def gender(self):
        """
        Method returns assumed gender of the person based on their name,
        using API from genderize.io
        """
        nameInfo = requests.get(urlBasic.format(personName=self.name())).json()
        gender = nameInfo['gender']
        return gender
