class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __len__(self):
        if self.next is None:
            return 1

        # iterative approach is more optimal in terms of space, but recursive one is less trivial
        return len(self.next) + 1


def find_intersection(head1, head2) -> Node:

    # the last node of intersecting lists are the same
    # it means that we can say if two lists are intersecting at the moment when we count lengths
    # but in sake of readability I will leave it as it is (count length in Node.__len__ method)
    len1 = len(head1)
    len2 = len(head2)

    if len1 > len2:
        short = head2
        long = head1
        diff = len1 - len2
    else:
        short = head1
        long = head2
        diff = len2 - len1

    for _ in range(diff):
        long = long.next

    while long and short:
        if long == short:
            return long
        long = long.next
        short = short.next

    return False


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    # 1 -> 2 -> 3 -> 4
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # 5 -> 6 -> 3 -> 4
    node5.next = node6
    node6.next = node3
    assert find_intersection(node1, node5) == node3

    # 5 -> 6 -> 1 -> 2 -> 3 -> 4
    node6.next = node1
    assert find_intersection(node1, node5) == node1

    # 5 -> 6
    node6.next = None
    assert not find_intersection(node1, node5)

    print('All tests are passed')
