def solution(arr: list, i: int = None) -> list:
    if len(arr) <= 1:
        return [arr]

    subsets = solution(arr[1:])
    sl = len(subsets)
    i = 0
    while i < sl:
        subset = [v for v in subsets[i]]
        subset.append(arr[0])
        subsets.append(subset)
        i += 1
    subsets.append([arr[0]])

    return subsets


if __name__ == '__main__':
    def main():
        arr = ['a']
        res = solution(arr)
        assert len(res) == 1
        assert res == [['a']]

        arr = ['a', 'b']
        res = solution(arr)
        assert len(res) == 3
        assert res == [
            ['b'],
            ['b', 'a'],
            ['a'],
        ]

        arr = ['a', 'b', 'c']
        res = solution(arr)
        assert len(res) == 7
        assert res == [['c'], ['c', 'b'], ['b'], ['c', 'a'], ['c', 'b', 'a'], ['b', 'a'], ['a']]


    # print(solution([1, 2, 3]))

    print('All tests are passed')

main()
