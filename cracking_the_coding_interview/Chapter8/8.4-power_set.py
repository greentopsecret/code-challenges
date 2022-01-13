def solution(arr: list, i: int = None) -> list:
    if i is None:
        i = 0

    if i == len(arr) - 1:
        return [[], [arr[i]]]

    subsets = solution(arr, i + 1)
    sl = len(subsets)
    j = 0
    while j < sl:
        subset = [v for v in subsets[j]]
        subset.append(arr[i])
        subsets.append(subset)
        j += 1

    return subsets


if __name__ == '__main__':
    def main():
        arr = ['a']
        res = solution(arr)
        assert len(res) == 2
        assert res == [[], ['a']]

        arr = ['a', 'b']
        res = solution(arr)
        assert len(res) == 4
        assert res == [[], ['b'], ['a'], ['b', 'a']]

        arr = ['a', 'b', 'c']
        res = solution(arr)
        assert len(res) == 8
        assert res == [[], ['c'], ['b'], ['c', 'b'], ['a'], ['c', 'a'], ['b', 'a'], ['c', 'b', 'a']]
        #
        # arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
        # res = solution(arr)
        # # print(res)


    print('All tests are passed')

    main()
