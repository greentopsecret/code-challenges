# 0101  5   =>  0011  3
# 10011 => 01110
def next_smaller_number(num: int):
    # return next_smaller_number_via_bit_manipulation(num)

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

    # # 10000011 => 01110000
    # num -= (1 << c1) - 1       # 10000000
    # num -= 1                   # 01111111
    # num -= (1 << (c0 - 1)) - 1 # 01110000

    return num - (1 << c1) - (1 << (c0 - 1)) + 1


def next_smaller_number_via_bit_manipulation(num: int):
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
    # return next_bigger_number_via_bit_manipulation(num)
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

    # num += pow(2, c0) - 1      # set all trailing zeros as ones
    # num += 1                   # clear all bits from right from first non-trailing zero
    # num += pow(2, c1 - 1) - 1  # add "c1-1" ones
    # return num

    return num + (1 << c0) + (1 << c1 - 1) - 1


def next_bigger_number_via_bit_manipulation(num: int):
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
        assert next_bigger_number(78) == 83  # 1001110 => 1010011
        assert next_bigger_number(43) == 45  # 101011 => 101101
        # print(next_bigger_number(43))

        assert next_smaller_number(7) is None
        assert next_smaller_number(6) == 5  # 110 => 101
        assert next_smaller_number(131) == 112  # 10000011 => 01110000
        assert next_smaller_number(19) == 14  # 10011 => 01110
        assert next_smaller_number(10115) == 10096  # 10011110000011 => 10011101110000
        assert next_smaller_number(11) == 7
        assert next_smaller_number(21) == 19
        assert next_smaller_number(38) == 37  # 100110 => 100101
        assert next_smaller_number(78) == 77  # 1001110 => 1001101
        # print(next_smaller_number(78))
        print('All tests are passed')


    # 1001110 = > 1010011
    # 1011110
    # 1010000
    # 1010011

    # 1001110
    # 1001111
    # 1010000

    main()
