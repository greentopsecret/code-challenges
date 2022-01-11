import math


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def build_binary_tree(arr):
    if len(arr) == 0:
        return None

    mid = math.ceil(len(arr) / 2) - 1
    root = TreeNode(arr[mid])
    root.left = build_binary_tree(arr[0:mid])
    root.right = build_binary_tree(arr[mid + 1:])

    return root


def find_first_common_ancestor(root, node1: TreeNode, node2: TreeNode):
    if not _contains(root, node1) or not _contains(root, node2):
        return None

    node, _ = _find_first_common_ancestor(root, node1, node2)

    return node


def _find_first_common_ancestor(root: TreeNode, node1: TreeNode, node2: TreeNode):
    if root is None:
        return None, False
    if root is node1 and root is node2:
        return root, True

    # node1_found = _contains(root, node1)
    # node2_found = _contains(root, node2)
    # if node1_found and not node2_found:
    #     return node1, False
    # if not node2_found and node2_found:
    #     return node2, False
    # if not node1_found and not node2_found:
    #     return None, False

    x, is_anc = _find_first_common_ancestor(root.left, node1, node2)
    if is_anc:
        return x, is_anc

    y, is_anc = _find_first_common_ancestor(root.right, node1, node2)
    if is_anc:
        return y, is_anc

    if x is not None and y is not None:
        return root, True

    if root == node1 or root == node2:
        return root, x is not None or y is not None

    return x if y is None else y, False


def _contains(root: TreeNode, node: TreeNode):
    if root is None:
        return False

    if root == node:
        return True

    return _contains(root.left, node) or _contains(root.right, node)


if __name__ == '__main__':
    def main():
        root = build_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        root.left.left.right.left = TreeNode(14)

        node1 = root.left.left.right  # 2 (not leaf)
        node2 = root.left.right.left  # 4 (leaf)

        assert find_first_common_ancestor(root, node1, node2) == root.left

        print('All tests are passed')


    main()
