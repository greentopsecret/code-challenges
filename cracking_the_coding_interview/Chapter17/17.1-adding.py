def solution(a: int, b: int) -> int:
    # return solution_iterative_a(a, b)
    # return solution_iterative_b(a, b)
    return solution_recursive(a, b)


def solution_iterative_a(a: int, b: int) -> int:
    result = 0
    carry = 0
    setter = 1

    # 0011
    # 0011
    # ----
    # 0110
    while a > 0 or b > 0 or carry > 0:
        a_bit = a & 1
        b_bit = b & 1
        s = a_bit ^ b_bit ^ carry
        carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
        if s:
            result |= setter
        setter <<= 1
        a >>= 1
        b >>= 1

    return result


def solution_iterative_b(a: int, b: int) -> int:
    result = 0

    while b > 0:
        result = a ^ b
        carry = (a & b) << 1
        a = result
        b = carry

    return result


def solution_recursive(a: int, b: int) -> int:
    if b <= 0:
        return a
    return solution_recursive(a ^ b, (a & b) << 1)


if __name__ == '__main__':
    def main():
        assert solution(3, 3) == 6
        assert solution(1, 3) == 4
        assert solution(0, 3) == 3
        assert solution(22, 27) == 49

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
