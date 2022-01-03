from collections import defaultdict


def is_permutation(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    frequencies = defaultdict(int)
    for i in range(len(str1)):
        char = str1[i]
        frequencies[char] = frequencies[char] + 1

    for i in range(len(str2)):
        char = str2[i]
        frequencies[char] -= 1
        if frequencies[char] < 0:
            return False

    return True


if __name__ == '__main__':
    assert is_permutation('abc', 'acb')
    assert is_permutation('abcc', 'acbc')
    assert not is_permutation('aabc', 'acb')
    assert not is_permutation('aabc', 'acbe')
    assert not is_permutation('abcd', 'abde')
