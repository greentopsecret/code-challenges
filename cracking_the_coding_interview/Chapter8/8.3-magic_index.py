import math
from typing import Union


def solution(arr: list) -> Union[int, None]:
    # return solution_recursive(arr, 0, len(arr) - 1)
    return solution_iterative_unique(arr)


def solution_iterative_unique(arr) -> Union[int, None]:
    """

    this solution works only for unique elements

    :param arr:
    :return:
    """
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = math.floor((i + j) / 2)
        if mid == arr[mid]:
            return mid
        if arr[mid] > mid:
            j = mid - 1
        if arr[mid] < mid:
            i = mid + 1
    return None


def solution_recursive(arr, i, j) -> Union[int, None]:
    if j < i:
        return None

    mid = math.floor((j + i) / 2)
    if mid == arr[mid]:
        return mid

    if arr[mid] > mid:
        return solution_recursive(arr, i, mid - 1)

    if arr[mid] < mid:
        return solution_recursive(arr, mid + 1, j)


if __name__ == '__main__':
    def main():
        assert solution([1, 2, 3]) is None
        assert solution([-5, -3, -1, 1, 4, 6, 8]) == 4
        assert solution([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]) == 7

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
