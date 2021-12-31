# https://leetcode.com/discuss/interview-question/883338/Facebook-or-Question

def merge_arrays(A, B):
    i = 0
    output = []
    aidx = []
    pa, pb = 0, 0
    while pa < len(A) and pb < len(B):
        if A[pa] < B[pb]:
            output.append(A[pa])
            aidx.append(i)
            i += 1
            pa += 1
        else:
            output.append(B[pb])
            i += 1
            pb += 1
    while pa < len(A):
        output.append(A[pa])
        aidx.append(i)
        i += 1
        pa += 1

    return aidx, output + B[pb:]


def solution(a, b):
    a_idx, merged = merge_arrays(a, b)

    # for each index calculate all diffs up to the previous element in original list
    # As we traverse through the list keep track of last index of item
    # from A
    max_length = 0
    diffs = {}
    a_idx = set(a_idx)
    for i in range(1, len(merged)):
        temp = {}
        for j in range(i - 1, -1, -1):
            d = merged[i] - merged[j]
            temp[(i, d)] = diffs.get((j, d), 1) + 1
            # stop when hit the last (first from right) element from list A
            if j in a_idx:
                temp.update(diffs)
                break
        max_length = max(max_length, max(temp.values()) if temp else 0)
        diffs = temp

    return max_length


if __name__ == '__main__':
    # assert solution([1, 4, 8, 17], [0, 9, 10, 12, 15, 16]) == 4
    assert solution([1], [2, 4, 6]) == 2
