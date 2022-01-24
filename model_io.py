from typing import Union
from os import PathLike


def read_wishes(file_handle: Union[str, PathLike]) -> str:
    """
    Reads wishes text from file_handle
    """
    wishes = ''
    for line in file_handle:
        wishes += line
    wishes2 = wishes[0:-1]
    return wishes2


def load_wishes(file_handle: Union[str, PathLike]) -> str:
    """
    Loads file from file_handle, and calls read function
    """
    with open(file_handle) as file:
        wishes = read_wishes(file)
    return wishes
