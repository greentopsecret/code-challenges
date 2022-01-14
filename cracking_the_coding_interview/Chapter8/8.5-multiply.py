def solution(a: int, b: int) -> int:
    # return solution_iterative(a if a < b else b, a if a >= b else b)
    # return solution_recursive_1(a if a < b else b, a if a >= b else b, {})
    return solution_recursive_2(a, b)


def solution_recursive_1(a: int, b: int, cache: dict) -> int:
    if b == 0:
        return 0
    if b == 1:
        return a

    if b not in cache.keys():
        b1 = 1
        while (b1 << 1) < b:
            b1 <<= 1

        b2 = b - b1
        res = solution_recursive_1(a, b1, cache) + solution_recursive_1(a, b2, cache)

        cache[b] = res

    return cache[b]


def solution_recursive_2(a: int, b: int) -> int:
    if a > b:
        a = a + b
        b = a - b
        a = a - b

    if a == 0:
        return 0
    if a == 1:
        return b

    a_half = a >> 1
    h1 = solution_recursive_2(a_half, b)
    h2 = h1 if a % 2 == 0 else solution_recursive_2(a - a_half, b)

    return h1 + h2


def solution_iterative(a: int, b: int) -> int:
    if b == 0:
        return 0
    if b == 1:
        return a

    power = 1
    res = a
    while power + power <= b:
        res <<= 1
        power += power

    diff1 = b - power
    diff2 = power + power - b
    if diff1 < diff2:
        for _ in range(diff1):
            res += a
    else:
        res <<= 1
        for _ in range(diff2):
            res -= a

    return res


if __name__ == '__main__':
    def main():
        assert solution(5, 2) == 10
        assert solution(2, 5) == 10
        assert solution(2, 7) == 14
        assert solution(2, 10) == 20
        assert solution(2, 4) == 8
        assert solution(3, 10) == 30
        assert solution(3, 1) == 3
        assert solution(1, 3) == 3
        assert solution(3, 0) == 0
        assert solution(0, 3) == 0
        assert solution(5, 15) == 75

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
