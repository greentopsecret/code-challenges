import math


# 110111001111
def flip_to_win(num: int) -> int:
    sequence = 0
    prev_sequence = 0
    max_len = 0
    while num > 0:
        bit = num % 2
        num = math.floor(num / 2)
        if bit:
            sequence += 1
        else:
            max_len = max(max_len, sequence + prev_sequence + 1)
            prev_sequence = sequence
            sequence = 0

    if prev_sequence > 0:
        max_len = max(max_len, sequence + prev_sequence + 1)
    else:
        max_len = sequence

    return max_len


if __name__ == '__main__':
    def main():
        assert flip_to_win(1775) == 8  # 11011101111
        assert flip_to_win(3535) == 6  # 110111001111
        assert flip_to_win(15) == 4  # 1111

        print('All tests are passed')


    main()
