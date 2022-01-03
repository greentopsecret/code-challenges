class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    # def __len__(self):
    #     if self.next is None:
    #         return 1
    #
    #     # iterative approach is more optimal in terms of space, but recursive one is less trivial
    #     return len(self.next) + 1

    def get_length_and_tail(self):
        cnt = 0
        node = self
        while node:
            cnt += 1
            node = node.next
        return cnt, node


def find_intersection(head1, head2) -> Node:
    len1, tail1 = head1.get_length_and_tail()
    len2, tail2 = head2.get_length_and_tail()

    if tail1 != tail2:
        return False

    if len1 > len2:
        short = head2
        long = head1
    else:
        short = head1
        long = head2

    for _ in range(abs(len2 - len1)):
        long = long.next

    while long != short:
        long = long.next
        short = short.next

    return long


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
