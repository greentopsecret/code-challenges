import math


def flip_to_win(num: int):
    if num == -1:
        return math.inf
    sequence = 0
    prev_sequence = 0
    prev_prev_sequence = 0
    max_len = 0
    current_bit = 0
    while num > 0:
        if (num & 1) != current_bit:
            if prev_sequence == 1:
                max_len = max(max_len, prev_prev_sequence + sequence + 1)
            elif prev_sequence > 1:
                max_len = max(max_len, prev_sequence + 1)
            prev_prev_sequence = prev_sequence
            prev_sequence = sequence
            sequence = 0
            current_bit = num & 1
        sequence += 1
        num >>= 1

    if prev_sequence == 1:
        max_len = max(max_len, prev_prev_sequence + sequence + 1)
    elif prev_sequence > 1:
        max_len = max(max_len, max(sequence, prev_sequence) + 1)
    elif prev_sequence < 1:
        max_len = max(max_len, sequence)

    return max_len


if __name__ == '__main__':
    def main():
        assert flip_to_win(1775) == 8  # 11011101111
        assert flip_to_win(3535) == 6  # 110111001111
        assert flip_to_win(28) == 4  # 11100
        assert flip_to_win(24) == 4  # 11000
        assert flip_to_win(15) == 4  # 1111
        assert flip_to_win(-1) == math.inf  # ...11111111111
        # assert flip_to_win(-11) == 6  # 11110101

        print('All tests are passed')


    main()
