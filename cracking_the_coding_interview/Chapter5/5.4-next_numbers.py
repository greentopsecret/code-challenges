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
def next_smallest_number(num: int):
    ones_cnt = get_ones_cnt(num)
    _next = num - 1
    while _next > 0 and get_ones_cnt(_next) != ones_cnt:
        _next = _next - 1
    return _next


def next_biggest_number(num: int):
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
        print('All tests are passed')


    main()
