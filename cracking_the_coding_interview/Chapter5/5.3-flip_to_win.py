import math


# 11011101111
# 110111001111
def flip_to_win(num: int):
    if num == -1:
        return math.inf

    current_sequence = 0
    prev_sequence = 0
    max_len = 0
    bits_cnt = 0
    while num > 0:
        bits_cnt += 1
        if (num & 1) == 1:
            current_sequence += 1
        else:
            prev_sequence = 0 if (num & 2) == 0 else current_sequence
            current_sequence = 0

        if current_sequence == bits_cnt:
            max_len = max(max_len, current_sequence)
        else:
            max_len = max(max_len, prev_sequence + current_sequence + 1)

        num >>= 1

    return max_len


if __name__ == '__main__':
    def main():
        assert flip_to_win(91) == 5  # 1011011
        assert flip_to_win(1775) == 8  # 11011101111
        assert flip_to_win(3535) == 6  # 110111001111
        assert flip_to_win(28) == 4  # 11100
        assert flip_to_win(24) == 3  # 11000
        assert flip_to_win(15) == 4  # 1111
        assert flip_to_win(-1) == math.inf  # ...11111111111
        # assert flip_to_win(-11) == 6  # 11110101

        print('All tests are passed')


    main()
