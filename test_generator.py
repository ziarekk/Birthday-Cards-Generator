from generator import Person


def test_init():
    person1 = Person('Andy')
    assert person1.name() == 'Andy'


def test_get_gender_M():
    person1 = Person('Tom')
    assert person1.gender() == 'male'


def test_get_gender_F():
    person1 = Person('Anna')
    assert person1.gender() == 'female'
