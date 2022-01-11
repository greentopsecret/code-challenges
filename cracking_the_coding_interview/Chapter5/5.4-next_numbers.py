import math


# 0000  0
# 0001  1
# 0010  2
# 0011  3
# 0100  4
# 0101  5
# 0110  6
# 0111  7
# 1000  8
# 1001  9
# 1010  10
# 1011  11
# 1100  12
# 1101  13
# 1110  14
# 1111  15

# 0101  5   =>  0011  3
def next_smallest_number(num: int):
    # find the first non-trailing one
    p = 0
    n = num
    while n > 0 and (n & 1) == 1:
        p += 1
        n >>= 1

    if n == 0:  # only ones in the input number
        return None

    while n > 0 and (n & 1) == 0:
        p += 1
        n >>= 1

    # set zero bit at "p" position
    num &= ~(1 << p)

    # set one bit at "p-1" position
    num |= 1 << (p - 1)

    return num


def next_biggest_number(num: int):
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
        assert next_smallest_number(6) == 5
        assert next_biggest_number(6) == 9

        assert next_smallest_number(11) == 7
        assert next_biggest_number(11) == 13

        assert next_smallest_number(7) is None
        print('All tests are passed')


    main()
