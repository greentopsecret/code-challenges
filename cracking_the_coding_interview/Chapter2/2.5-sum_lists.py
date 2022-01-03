class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '%s (next=%s)' % (str(self.value),
                                 str(self.next.value) if self.next else None)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node: Node):
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return self

    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)


def sum_lists(a, b):
    carry = 0
    head = None
    tail = None
    while True:
        d = 0

        if a and b:
            d = a.value + b.value
        elif a:
            d = a.value
        elif b:
            d = b.value
        else:
            break
        d += carry
        carry = 1 if d > 9 else 0
        node = Node(d % 10)
        if tail:
            tail.next = node
            tail = tail.next
        else:
            tail = node
            head = tail
        a = a.next if a else None
        b = b.next if b else None

    return head


def sum_reverse_lists(a, b) -> Node:
    _, _, node, _ = _sum_reverse_lists_recursive(a, b, 0, 0)

    return node


def _sum_reverse_lists_recursive(input_a, input_b, idx_a, idx_b) -> tuple[int, int, Node, int]:
    if input_a.next is None and input_b.next is None:
        s = input_a.value + input_b.value
        return 0, 0, Node(s % 10), 1 if s > 9 else 0

    if input_a.next is None and input_b.next is not None:
        i_a = input_a
        i_b = input_b.next
        idx_b += 1
    elif input_a.next is not None and input_b.next is None:
        i_a = input_a.next
        i_b = input_b
        idx_a += 1
    else:
        i_a = input_a.next
        i_b = input_b.next
        idx_a += 1
        idx_b += 1

    idx_a, idx_b, sum_node, carry = _sum_reverse_lists_recursive(
        i_a,
        i_b,
        idx_a,
        idx_b
    )

    if idx_a == idx_b:
        s = input_a.value + input_b.value + carry
        n = Node(s % 10)
        n.next = sum_node
        return idx_a, idx_b, n, 1 if s > 9 else 0
    else:
        return idx_a, idx_b, sum_node, carry


if __name__ == '__main__':
    # list617 = LinkedList() \
    #     .add(7) \
    #     .add(1) \
    #     .add(6)

    head617 = Node(7)
    head617.next = Node(1)
    head617.next.next = Node(6)

    # list295 = LinkedList() \
    #     .add(5) \
    #     .add(9) \
    #     .add(2)

    head295 = Node(5)
    head295.next = Node(9)
    head295.next.next = Node(2)

    result = sum_lists(head617, head295)

    head912 = Node(2)
    head912.next = Node(1)
    head912.next.next = Node(9)

    # ll = LinkedList()
    # ll.add(result)
    # print(str(ll))

    assert str(LinkedList().add(result)) == str(LinkedList().add(head912))

    head1246 = Node(1)
    head1246.next = Node(2)
    head1246.next.next = Node(4)
    head1246.next.next.next = Node(6)

    head56 = Node(5)
    head56.next = Node(6)

    result = sum_reverse_lists(head1246, head56)

    head1302 = Node(1)
    head1302.next = Node(3)
    head1302.next.next = Node(0)
    head1302.next.next.next = Node(2)

    # ll = LinkedList()
    # ll.add(result)
    # print(str(ll))

    assert str(LinkedList().add(result)) == str(LinkedList().add(head1302))
