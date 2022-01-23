def read_wishes(file_handle):
    """
    Reads wishes text from file_handle.txt
    """
    wishes = ''
    for line in file_handle:
        wishes += line
    wishes2 = wishes[0:-1]
    return wishes2


def load_wishes(file_handle):
    """
    Loads wishes text from file_handle
    """
    with open(file_handle) as file:
        wishes = read_wishes(file)
    return wishes
