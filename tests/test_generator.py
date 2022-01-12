from generator import Person


def test_init():
    card = Person('Andy')
    assert card.name() == 'Andy'


def test_get_gender_M():
    card = Person('Tom')
    assert card.gender() == 'male'


def test_get_gender_F():
    card = Person('Anna')
    assert card.gender() == 'female'
