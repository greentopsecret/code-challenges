from collections import defaultdict


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def _collect_level_values(node: Node, data: {}, level: int):
    if not node:
        return

    if level in data.keys():
        data[level].append(node.value)
    else:
        data[level] = [node.value]

    _collect_level_values(node.left, data, level + 1)
    _collect_level_values(node.right, data, level + 1)


def calculate_level_average_dfs(root: Node):
    if not root:
        return []

    r = []
    data = {}
    _collect_level_values(root, data, 0)
    level = 0
    while level in data:
        r.append(sum(data[level]) / len(data[level]))
        level += 1

    return r


def calculate_level_average_bfs(root: Node) -> list:
    result = []

    if not root:
        return result

    queue = [root]
    _len = len(queue)
    while _len > 0:
        s = 0
        for _ in range(_len):
            n = queue.pop(0)
            s += n.value
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        result.append(s / _len)
        _len = len(queue)

    return result


# queue=[4], result=[4]             | queue=[7, 9]
# queue=[7, 9], result=[4, 8]       | queue=[10, 2, 6]
# queue=[10, 2, 6], result=[4, 8, 6]| queue=[...]


if __name__ == '__main__':
    node = Node(4)
    node.left = Node(7)
    node.right = Node(9)
    node.left.left = Node(10)
    node.left.right = Node(2)
    node.right.right = Node(6)
    node.left.right.right = Node(6)
    node.left.right.right.left = Node(2)

    assert [4, 8, 6, 6, 2] == calculate_level_average_dfs(node)
    assert [4, 8, 6, 6, 2] == calculate_level_average_bfs(node)
