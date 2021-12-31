from collections import defaultdict
from math import sqrt


def is_palindrome_permutation_2(string: str):
    string = string.lower()
    vector = 0
    for i in range(len(string)):
        char = string[i]
        if char == ' ':
            continue

        index = ord(char) - ord('a')
        mask = 1 << index
        if vector & mask:
            vector ^= mask  # vector &= ~mask
        else:
            vector |= mask

    return vector & (vector - 1) == 0


def is_palindrome_permutation_1(string: str):
    string = string.lower()
    chars = defaultdict(int)
    for i in range(len(string)):
        char = string[i]
        if char == ' ':
            continue
        chars[char] += 1
        if chars[char] == 2:
            del chars[char]

    return len(chars.keys()) < 2


if __name__ == '__main__':
    assert is_palindrome_permutation_2('Tact Coa')
    assert is_palindrome_permutation_2('TactCoapapa')
    assert not is_palindrome_permutation_2('Tact Coaa')
