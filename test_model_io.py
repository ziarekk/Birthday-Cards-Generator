from model_io import read_wishes, load_wishes
from io import StringIO


def test_read_wishes():
    data = 'Wishes\n to you\n my friend!\n'
    file_handle = StringIO(data)
    wishes = read_wishes(file_handle)
    assert wishes == 'Wishes\n to you\n my friend!'


def test_load_wishes(mocker):
    test_data = 'Wishes\n to you\n my friend!\n'
    m = mocker.patch('builtins.open', mocker.mock_open(read_data=test_data))
    wishes = load_wishes('foo')
    m.assert_called_once_with('foo')
    assert wishes == 'Wishes\n to you\n my friend!'
