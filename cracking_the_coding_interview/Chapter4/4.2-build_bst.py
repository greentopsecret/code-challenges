import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_bst(arr):
    return _build_bst(arr, 0, len(arr))


def _build_bst(arr, start, end):
    if start >= end:
        return None

    mid = math.floor((end + start) / 2)
    root = Node(arr[mid])
    root.left = _build_bst(arr, start, mid)
    root.right = _build_bst(arr, mid + 1, end)

    return root


if __name__ == '__main__':
    def main():
        root = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        assert root.value == 7
        assert root.left.value == 4
        assert root.left.left.value == 2
        assert root.left.left.left.value == 1
        assert root.left.left.right.value == 3
        assert root.left.left.right.left is None
        assert root.left.left.right.right is None
        assert root.left.right.value == 6
        assert root.left.right.left.value == 5
        assert root.left.right.left.left is None
        assert root.left.right.left.right is None
        assert root.left.right.right is None
        assert root.right.value == 11
        assert root.right.left.value == 9
        assert root.right.left.left.value == 8
        assert root.right.left.right.value == 10
        assert root.right.left.right.left is None
        assert root.right.left.right.right is None
        assert root.right.right.value == 13
        assert root.right.right.left.value == 12
        assert root.right.right.left.left is None
        assert root.right.right.left.right is None
        assert root.right.right.right is None
        print('All tests are passed')


    main()
