from generator import Person, getItem
from constants import Frames, Wishes, backgroundImages


def test_init_Person_M():
    person1 = Person('Andy')
    assert person1.name() == 'Andy'
    assert person1.gender() == 'male'


def test_init_Person_F():
    person1 = Person('Anna')
    assert person1.name() == 'Anna'
    assert person1.gender() == 'female'


def test_init_Person_wrong_data():
    person1 = Person('Jan Paweł 2')
    assert person1.gender() == 'None'


def test_getItem_frame_typical(monkeypatch):
    def random_frame(list):
        return 'frame_3'

    monkeypatch.setattr('generator.random.choice', random_frame)
    frame = getItem('female', Frames)
    assert frame == 'frame_3'


def test_getItem_background_typical(monkeypatch):
    def random_background(list):
        return 'back_9'

    monkeypatch.setattr('generator.random.choice', random_background)
    background = getItem('male', backgroundImages)
    assert background == 'back_9'


def test_getItem_wishes_typical(monkeypatch):
    def random_wishes(list):
        return 'wishes_1'

    monkeypatch.setattr('generator.random.choice', random_wishes)
    wishes = getItem('male', Wishes)
    assert wishes == 'wishes_1'


def test_getItem_frame_random():
    frame = getItem('female', Frames)
    fGender = Frames[frame]['gender']
    assert fGender == 'unisex' or fGender == 'female'


def test_getItem_wishes_random():
    wishes = getItem('male', Wishes)
    wGender = Wishes[wishes]['gender']
    assert wGender == 'unisex' or wGender == 'male'


def test_getItem_background_random():
    backImg = getItem('male', backgroundImages)
    bGender = backgroundImages[backImg]['gender']
    assert bGender == 'unisex' or bGender == 'male'
