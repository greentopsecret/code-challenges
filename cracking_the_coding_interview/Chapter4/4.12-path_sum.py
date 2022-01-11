class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def paths_sum(root: TreeNode, s: int):
    pass


if __name__ == '__main__':
    def main():
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(1)
        root.right = TreeNode(-3)
        root.right.right = TreeNode(11)

        assert 3 == paths_sum(root, 8)


    main()
