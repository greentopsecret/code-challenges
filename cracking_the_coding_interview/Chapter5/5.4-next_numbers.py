import math


# 00000  0
# 00001  1
# 00010  2
# 00011  3
# 00100  4
# 00101  5
# 00110  6
# 00111  7
# 01000  8
# 01001  9
# 01010  10
# 01011  11
# 01100  12
# 01101  13
# 01110  14
# 01111  15
# 10000  16
# 10001  17
# 10010  18
# 10011  19
# 10100  20
# 10101  21
# 10110  22
# 10111  23
# 11000  24
# 11001  25
# 11010  26
# 11011  27
# 11100  28
# 11101  29
# 11110  30
# 11111  31

# 0101  5   =>  0011  3
# 10011 => 01110
def next_smaller_number(num: int):
    # find the first non-trailing one
    c0 = c1 = 0
    n = num
    while n > 0 and (n & 1) == 1:
        c1 += 1
        n >>= 1

    if n == 0:  # only ones in the input number
        return None

    while n > 0 and (n & 1) == 0:
        c0 += 1
        n >>= 1

    p = c0 + c1

    # set zero bit at "p" position
    num &= ~(1 << p)

    # reset bits on the right from "p"
    num &= ~0 << p  # ~((1 << p) - 1)

    # set "c1 + 1" ones on the right from "p"
    mask = (1 << (c1 + 1)) - 1
    mask <<= c0 - 1
    num |= mask

    return num


def next_bigger_number(num: int):
    if num == 0:
        return None

    # count number of ones and zeros before first non-trailing zero
    c0 = c1 = 0
    c = num
    while c > 0 and (c & 1) == 0:
        c0 += 1
        c >>= 1

    while c > 0 and (c & 1) == 1:
        c1 += 1
        c >>= 1

    # set one into the first non-trailing zero
    p = c0 + c1
    num |= 1 << p

    # put zeros to all bits on the right from "p"
    mask = ~((1 << p) - 1)
    num &= mask

    # put c1-1 ones to the right from "p"
    mask = (1 << (c1 - 1)) - 1
    num |= mask

    return num


def next_smallest_number_bruteforce(num: int):
    ones_cnt = get_ones_cnt(num)
    _next = num - 1
    while _next > 0 and get_ones_cnt(_next) != ones_cnt:
        _next = _next - 1
    return _next if _next > 0 else None


def next_biggest_number_bruteforce(num: int):
    ones_cnt = get_ones_cnt(num)
    _next = num + 1
    while get_ones_cnt(_next) != ones_cnt:
        _next = _next + 1
    return _next


def get_ones_cnt(num: int):
    cnt = 0
    while num > 0:
        if (num & 1) == 1:
            cnt += 1
        num >>= 1

    return cnt


if __name__ == '__main__':
    def main():
        assert next_bigger_number(6) == 9
        assert next_bigger_number(11) == 13

        assert next_smaller_number(7) is None
        assert next_smaller_number(6) == 5
        assert next_smaller_number(19) == 14  # 10011 => 01110
        assert next_smaller_number(10115) == 10096  # 10011110000011 => 10011101110000
        assert next_smaller_number(11) == 7
        assert next_smaller_number(21) == 19
        print('All tests are passed')


    main()
