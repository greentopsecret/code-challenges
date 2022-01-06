import math
from queue import SimpleQueue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __len__(self):
        if self.next is None:
            return 1

        return len(self.next) + 1


def build_bst(arr):
    if len(arr) == 0:
        return None

    mid = math.ceil(len(arr) / 2) - 1
    root = TreeNode(arr[mid])
    root.left = build_bst(arr[0:mid])
    root.right = build_bst(arr[mid + 1:])

    return root


def list_of_depths_bfs(root):
    queue = SimpleQueue()
    queue.put(root)

    result = []
    while not queue.empty():
        cnt = queue.qsize()
        t_node = queue.get()
        ll_node = LinkedListNode(t_node.value)
        result.append(ll_node)
        if t_node.left:
            queue.put(t_node.left)
        if t_node.right:
            queue.put(t_node.right)
        for _ in range(1, cnt):
            t_node = queue.get()
            ll_node.next = LinkedListNode(t_node.value)
            ll_node = ll_node.next
            if t_node.left:
                queue.put(t_node.left)
            if t_node.right:
                queue.put(t_node.right)

    return result


if __name__ == '__main__':
    def main():
        root = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

        lists = list_of_depths_bfs(root)
        assert len(lists) == 4
        assert len(lists[0]) == 1
        assert len(lists[1]) == 2
        assert len(lists[2]) == 4
        assert len(lists[3]) == 6

        print('All tests are passed')

    main()
