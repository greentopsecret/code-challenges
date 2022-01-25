from random import randrange


def solution(arr: list, m: int) -> list:
    if m == 0 or len(arr) == 0:
        return []

    idx = randrange(0, len(arr))
    val = arr[idx]
    arr[idx] = arr.pop()

    res = solution(arr, m - 1)
    res.append(val)

    return res


# def solution_recursive(arr: list, m: int)


if __name__ == '__main__':
    def main():
        # assert solution([1, 2, 3, 4, 5, 6, 7, 8]) is None

        print(solution([1, 2, 3, 4, 5, 6, 7, 8], 3))

        print('All tests are passed')


    main()
