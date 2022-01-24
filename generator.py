from PySide2.QtGui import QPixmap
from PIL import Image, ImageQt
from PIL import ImageDraw, ImageFont

from constants import Frames, backgroundImages, Wishes
from constants import mainFont, fntSrc
from constants import urlBasic

from model_io import load_wishes

import requests
import random


def getItem(gender: str, dictionary: dict) -> str:
    """
    Function randomly chooses item from the dictionary.
    Returns dictionary key.
    """
    itemKey = 'buffer'
    itemGender = dictionary[itemKey]['gender']
    while itemGender != gender and itemGender != 'unisex':
        itemKey = random.choice(list(dictionary))
        itemGender = dictionary[itemKey]['gender']

    return itemKey


def setBaseImage(person: 'Person', background: 'Image', wishes: str):
    """
    Function prepares basic attributes of the bithday card.
    """
    frame = getItem(person.gender(), Frames)
    txt = Image.new("RGBA", background.size, (255, 255, 255, 0))
    fntSize = Wishes[wishes]['fntSize']
    font = ImageFont.truetype(fntSrc, fntSize)
    with Image.open(Frames[frame]['source']) as frame_block:
        base = Image.alpha_composite(background, frame_block)

    return base, txt, font


def drawText(txt: 'Image', wishes: str, font: 'ImageFont'):
    """
    Draws text of the wishes in the center spot of the card.
    """
    draw = ImageDraw.Draw(txt)
    text = load_wishes(Wishes[wishes]['source'])
    boundingBox = [150, 150, 1050, 1050]
    shadowFont = Wishes[wishes]['shadowColor']
    x1, y1, x2, y2 = boundingBox
    w, h = draw.textsize(text, font=font)
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    draw.text((x-4, y-4), text, align='center', font=font, fill=shadowFont)
    draw.text((x, y), text, align='center', font=font, fill=mainFont)

    return txt


def combineImage(person: 'Person', base: 'Image', wishes: str) -> Image:
    """
    Combines ready-to-use card image from base components.
    """
    base, txt, font = setBaseImage(person, base, wishes)
    txt = drawText(txt, wishes, font)
    pilImage = Image.alpha_composite(base, txt)

    return pilImage


def imageConversion(pilImage: 'Image') -> QPixmap:
    """
    Function converts PIL.Image to QPixamp
    """
    qtImage = ImageQt.ImageQt(pilImage)
    qtPixmap = QPixmap.fromImage(qtImage)
    return qtPixmap


def generate_Card(person: 'Person'):
    """
    Function generates Birthday Card.
    """
    backgroundImg = getItem(person.gender(), backgroundImages)
    source = backgroundImages[backgroundImg]['source']
    wishes = getItem(person.gender(), Wishes)

    with Image.open(source).convert("RGBA") as background:
        pilImage = combineImage(person, background, wishes)
        qtPixmap = imageConversion(pilImage)

    return (pilImage, qtPixmap)


class Person():
    """
    Class Person - holds info about the jubilarian.
    :param name: person's name
    :type name: str
    """
    def __init__(self, name: 'str'):
        self._name = name

    def name(self) -> str:
        return self._name

    def gender(self) -> str:
        """
        Returns assumed gender of the person,
        """
        nameInfo = requests.get(urlBasic.format(personName=self.name())).json()
        gender = nameInfo['gender']
        if not gender:
            gender = 'unisex'
        return gender
