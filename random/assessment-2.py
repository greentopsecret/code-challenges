def minMoves(arr):
    # check input
    if len(arr) == 0:
        return 0

    # find least frequent digit
    ones = 0
    zeros = 0
    for i in arr:
        if i:
            ones += 1
        else:
            zeros += 1
    digit_to_move = 0 if ones > zeros else 1

    # how many swaps will it take to sort digit_to_move to the left?
    l = -1
    i = 0
    cnt_l = 0
    while i < len(arr):
        if arr[i] == digit_to_move:
            l += 1
            cnt_l += i - l
            i += 1
        else:
            i += 1

    # how many swaps will it take to sort digit_to_move to the right?
    r = len(arr)
    i = len(arr) - 1
    cnt_r = 0
    while i >= 0:
        if arr[i] == digit_to_move:
            r -= 1
            cnt_r += r - i
            i -= 1
        else:
            i -= 1

    return min(cnt_l, cnt_r)


if __name__ == '__main__':
    def main():
        assert minMoves([0, 1, 0, 1]) == 1
        assert minMoves([0, 0, 0, 0, 1, 1, 1, 1]) == 0
        assert minMoves([0, 1, 0, 1, 1, 1, 1, 0]) == 6
        assert minMoves([1, 1, 1, 1, 0, 1, 0, 1]) == 3

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
