import math
from typing import Union


def solution(arr: list) -> Union[int, None]:
    # return solution_recursive_unique(arr, 0, len(arr) - 1)
    # return solution_iterative_unique(arr)

    res = solution_recursive_non_unique(arr, 0, len(arr) - 1)
    return None if res is False else res


def solution_recursive_non_unique(arr, start, end) -> Union[int, bool]:
    if end < start:
        return False

    mid = math.floor((end + start) / 2)
    mid_value = arr[mid]
    if mid == mid_value:
        return mid

    if mid_value > mid:
        res = solution_recursive_non_unique(arr, start, mid - 1)
        if res:
            return res
        if mid_value > 0 and mid_value < len(arr):
            return solution_recursive_non_unique(arr, mid_value, end)

    if mid_value < mid:
        res = solution_recursive_non_unique(arr, mid + 1, end)
        if res:
            return res

        if mid_value > 0 and mid_value < len(arr):
            return solution_recursive_non_unique(arr, start, mid_value)


def solution_iterative_unique(arr) -> Union[int, None]:
    """

    this solution works only for unique elements

    :param arr:
    :return:
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = math.floor((start + end) / 2)
        mid_value = arr[mid]
        if mid == mid_value:
            return mid
        if mid_value > mid:
            end = mid - 1
        if mid_value < mid:
            start = mid + 1
    return None


def solution_recursive_unique(arr, start, end) -> Union[int, None]:
    """

    this solution works only for unique elements

    :param arr:
    :return:
    """
    if end < start:
        return None

    mid = math.floor((end + start) / 2)
    mid_value = arr[mid]
    if mid == mid_value:
        return mid

    if mid_value > mid:
        return solution_recursive_unique(arr, start, mid - 1)

    if mid_value < mid:
        return solution_recursive_unique(arr, mid + 1, end)


if __name__ == '__main__':
    def main():
        assert solution([1, 2, 3]) is None
        assert solution([-5, -3, -1, 1, 4, 6, 8]) == 4
        assert solution([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]) == 7
        assert solution([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]) == 7

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
