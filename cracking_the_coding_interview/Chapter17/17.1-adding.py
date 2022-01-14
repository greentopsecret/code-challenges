def solution(a: int, b: int) -> int:
    result = 0
    rem = 0
    setter = 1

    # 0011
    # 0011
    # ----
    # 0110
    while a > 0 or b > 0 or rem > 0:
        a_bit = a & 1
        b_bit = b & 1
        s = a_bit ^ b_bit ^ rem
        rem = (a_bit & b_bit) | (a_bit & rem) | (b_bit & rem)
        if s:
            result |= setter
        setter <<= 1
        a >>= 1
        b >>= 1

    return result


if __name__ == '__main__':
    def main():
        assert solution(3, 3) == 6
        assert solution(1, 3) == 4
        assert solution(0, 3) == 3
        assert solution(12, 35) == 47

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
