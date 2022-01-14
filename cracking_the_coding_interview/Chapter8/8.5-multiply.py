def solution(a: int, b: int) -> int:
    return solution_iterative(a, b)


def solution_iterative(a: int, b: int) -> int:
    if b == 0:
        return 0

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
        assert solution(2, 5) == 10
        assert solution(2, 7) == 14
        assert solution(2, 10) == 20
        assert solution(2, 4) == 8
        assert solution(3, 10) == 30
        assert solution(3, 1) == 3
        assert solution(3, 0) == 0
        assert solution(5, 15) == 75

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
