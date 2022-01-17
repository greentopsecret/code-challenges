def sorted_merge(a: list, b: list) -> list:
    idx_a = 0
    while idx_a < (len(a) - 1) and a[idx_a + 1] is not None:
        idx_a += 1

    idx_b = len(b) - 1
    idx_last = len(a) - 1
    while idx_b >= 0:
        if a[idx_a] and a[idx_a] > b[idx_b]:
            a[idx_last] = a[idx_a]
            idx_a -= 1
        else:
            a[idx_last] = b[idx_b]
            idx_b -= 1
        idx_last -= 1

    return a


if __name__ == '__main__':
    def main():
        assert sorted_merge([1, 6, 9, 13, 14, None, None, None, None], [2, 4, 7, 15]) == [1, 2, 4, 6, 7, 9, 13, 14, 15]
        assert sorted_merge([2], []) == [2]
        assert sorted_merge([None], [2]) == [2]

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
