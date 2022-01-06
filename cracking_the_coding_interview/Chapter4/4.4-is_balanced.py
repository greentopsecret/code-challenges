import math


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __len__(self):
        if self.next is None:
            return 1

        return len(self.next) + 1

    def __str__(self):
        return self.value


def build_bst(arr):
    if len(arr) == 0:
        return None

    mid = math.ceil(len(arr) / 2) - 1
    root = TreeNode(arr[mid])
    root.left = build_bst(arr[0:mid])
    root.right = build_bst(arr[mid + 1:])

    return root


def is_balanced(node: TreeNode) -> bool:
    return _is_balanced(node) != -1


def _is_balanced(node: TreeNode) -> int:
    if node.left is None and node.right is None:
        return 1

    left_depth = None
    if node.left:
        left_depth = _is_balanced(node.left)
        if left_depth == -1:
            return left_depth

    right_depth = None
    if node.right:
        right_depth = _is_balanced(node.right)
        if right_depth == -1:
            return right_depth

    if left_depth is None:
        left_depth = right_depth
    if right_depth is None:
        right_depth = left_depth

    return max(left_depth, right_depth) + 1 if abs(left_depth - right_depth) <= 1 else -1


if __name__ == '__main__':
    def main():
        root = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        assert is_balanced(root)

        root.left.left.right.left = TreeNode(14)
        assert is_balanced(root)

        root.left.left.right.left.left = TreeNode(15)
        assert not is_balanced(root)

        print('All tests are passed')


    main()
