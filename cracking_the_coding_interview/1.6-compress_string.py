def compress(string: str):
    if not len(string):
        return ''

    if len(string) == 1:
        return string

    result = []
    result_len = 0
    _len = 0
    for i in range(0, len(string)):
        _len += 1
        if i + 1 == len(string) or string[i] != string[i + 1]:
            p = string[i] + str(_len)
            result.append(p)
            result_len += len(p)
            _len = 0

    return ''.join(result) if len(string) > result_len else string


if __name__ == '__main__':
    print(compress('aaaabbc'))
    assert compress('aaaabbc') == 'a4b2c1'
    assert compress('aaaabbbc') == 'a4b3c1'
    assert compress('abbc') == 'abbc'
    assert compress('aabcccccaaa') == 'a2b1c5a3'
