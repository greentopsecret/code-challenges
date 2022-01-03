def is_rotation(str1: str, str2: str):
    return str2 in ''.join([str1, str1])


if __name__ == '__main__':
    assert is_rotation('erbottlewat', 'waterbottle')
    assert not is_rotation('erbottlewaf', 'waterbottle')