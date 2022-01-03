class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def get_loop_start(head: Node) -> Node:
    point_in_loop = get_point_in_loop(head)
    if point_in_loop is False:
        return False

    loop_length = find_loop_length(point_in_loop)

    p1 = p2 = head
    for _ in range(loop_length):
        p1 = p1.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


def get_point_in_loop(head: Node) -> Node:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return fast

    return False


def find_loop_length(node: Node) -> int:
    cnt = 1
    n = node.next
    while node != n:
        n = n.next
        cnt += 1
    return cnt


if __name__ == '__main__':
    root = Node('A')
    root.next = Node('B')
    root.next.next = Node('C')
    root.next.next.next = Node('D')
    root.next.next.next.next = Node('E')
    root.next.next.next.next.next = root.next.next  # Node('C')
    assert get_loop_start(root) == root.next.next

    root = Node('A')
    root.next = Node('B')
    root.next.next = Node('C')
    root.next.next.next = Node('D')
    root.next.next.next.next = Node('E')
    root.next.next.next.next.next = Node('F')
    assert get_loop_start(root) is False

    print('All checks are passed')
