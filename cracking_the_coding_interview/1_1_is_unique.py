def is_unique(string: str):
    if not len(string):
        return True

    a = ord('a')

    seen_characters = 0
    string = string.lower()
    for i in range(len(string)):
        char_code = ord(string[i]) - a
        if seen_characters & (1 << char_code):
            return False
        seen_characters = seen_characters | (1 << char_code)

    return True


if __name__ == '__main__':
    assert is_unique('')
    assert is_unique('abcd')
    assert not is_unique('abcddefg')
