def triple_step(n) -> int:
    # return triple_step_recursive(n)
    return triple_step_dp(n)


def triple_step_dp(n) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    a = 1
    b = 1
    c = 2
    for _ in range(3, n):
        d = a + b + c
        a = b
        b = c
        c = d

    return a + b + c


def triple_step_recursive(n) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


if __name__ == '__main__':
    def main():
        assert triple_step(1) == 1
        assert triple_step(2) == 2
        assert triple_step(3) == 4
        assert triple_step(15) == 5768
        assert triple_step(150) == 3081058855986474528462647721608166932600

        # print(triple_step(150))

        print('All tests are passed')


    main()
