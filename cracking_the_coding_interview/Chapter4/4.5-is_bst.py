import math


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def build_bst(arr):
    if len(arr) == 0:
        return None

    mid = math.ceil(len(arr) / 2) - 1
    root = TreeNode(arr[mid])
    root.left = build_bst(arr[0:mid])
    root.right = build_bst(arr[mid + 1:])

    return root


def is_bst_a(node: TreeNode):
    result, _, _ = _is_bst_a(node)
    return result


def _is_bst_a(node: TreeNode):
    if node is None:
        return True, math.inf, -math.inf

    left_result, left_min_value, left_max_value = _is_bst_a(node.left)
    if not left_result or left_max_value > node.value:
        return False, 0, 0

    right_result, right_min_value, right_max_value = _is_bst_a(node.right)
    if not right_result or right_min_value <= node.value:
        return False, 0, 0

    return True, min(left_min_value, right_min_value, node.value), max(left_max_value, right_max_value, node.value)


def is_bst_b(node: TreeNode, min_val: int = None, max_val: int = None):
    if node is None:
        return True

    if min_val and min_val >= node.value:
        return False

    if max_val and max_val < node.value:
        return False

    return is_bst_b(node.left, min_val, node.value) and is_bst_b(node.right, node.value, max_val)


def is_bst_c(node: TreeNode):
    result, _ = _is_bst_c(node, None)
    return result


def _is_bst_c(node: TreeNode, prev: TreeNode = None):
    if node is None:
        return True, prev

    result, prev = _is_bst_c(node.left, prev)
    if not result:
        return result, prev

    if prev and prev.value > node.value:
        return False, node

    if node.right:
        if node.right.value <= node.value:
            return False, node

    result, prev = _is_bst_c(node.right, node)
    return result, prev


if __name__ == '__main__':
    def main():
        root = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        assert is_bst_a(root)
        assert is_bst_b(root)
        assert is_bst_c(root)

        root = build_bst([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        assert not is_bst_a(root)
        assert not is_bst_b(root)
        assert not is_bst_c(root)

        root = build_bst([1, 2, 3, 4, 5, 6, 7])
        assert is_bst_a(root)
        assert is_bst_b(root)
        assert is_bst_c(root)

        root = build_bst([1, 2, 3, 4, 6, 6, 7])
        assert is_bst_a(root)
        assert is_bst_b(root)
        assert is_bst_c(root)

        root = build_bst([1, 2, 3, 4, 5, 6, 6])
        assert not is_bst_a(root)
        assert not is_bst_b(root)
        assert not is_bst_c(root)

        root = build_bst([1, 2, 5, 4, 5, 6, 7])
        assert not is_bst_a(root)
        assert not is_bst_b(root)
        assert not is_bst_c(root)

        print('All tests are passed')


    main()
