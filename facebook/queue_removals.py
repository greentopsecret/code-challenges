from operator import itemgetter


def find_positions_list(arr: list[int], x: int) -> list[int]:
    """
    Solution from https://leetcode.com/discuss/interview-question/1039925/Facebook-Practice-question-or-Queue-Removals
    :param arr:
    :param x:
    :return:
    """
    q = [(v, i) for i, v in enumerate(arr, start=1)]
    output = []

    for _ in range(x):
        tmp = q[:x]
        max_item = max(tmp, key=itemgetter(0))
        output.append(max_item[1])
        tmp.remove(max_item)
        # decrement value by 1 for each item unless it's 0
        tmp = [(v - 1, i) if v > 0 else (v, i) for v, i in tmp]
        q = q[x:] + tmp
    return output


def queue_removals(arr, x):
    head = 0
    _len = len(arr)
    x = min(x, _len)
    result = []
    for _ in range(x):
        max_value = -1
        max_idx = -1
        i = 0
        r = min(x, _len - len(result))
        while i < r:
            cur_val = arr[head]
            if cur_val == -1:
                head = (head + 1) % _len
                continue
            arr[head] = max(0, arr[head] - 1)
            if cur_val > max_value:
                max_value = cur_val
                max_idx = head
            i += 1
            head = (head + 1) % _len
        arr[max_idx] = -1
        result.append(max_idx + 1)

    return result


if __name__ == '__main__':
    # assert find_positions_list([1, 2, 2, 3, 4, 5], 5) == [5, 6, 4, 1, 2]
    assert queue_removals([1, 2, 2, 3, 4, 5], 5) == [5, 6, 4, 1, 2]
    assert queue_removals([2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4], 4) == [2, 5, 10, 13]
    print('All tests are passed')
