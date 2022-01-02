# A -> B -> C -> D; offset=2
# _get_from_the_end_recursive(A, 1, 0)
#   _get_from_the_end_recursive(B, 1, 0)
#       _get_from_the_end_recursive(C, 1, 0)
#           _get_from_the_end_recursive(D, 1, 0)
#               _get_from_the_end_recursive(None, 1, 0)
#               => None, 0
#           => None, 1
#       => C, 2
#   => C, 3

def _get_from_the_end_recursive(head, offset, idx):
    if head is None:
        return head, idx  # None, 0

    node, idx = _get_from_the_end_recursive(head.next, offset, idx)
    if idx == offset:
        return head, idx + 1

    return node, idx + 1


def get_from_the_end_recursive(node, offset):
    node, _ = _get_from_the_end_recursive(node, offset, 0)

    return node.value if node else None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None or self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self

    def get_from_the_end(self, offset):

        # return get_from_the_end_recursive(self.head, offset)

        if self.head is None:
            return None

        cnt = 0
        p1 = self.head
        while cnt < offset:
            cnt += 1
            p1 = p1.next
            if p1 is None:
                return None

        p2 = self.head
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next

        return p2.value if p2 else None

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return ' -> '.join(values)


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return '%s (next=%s)' % (self.value, self.next.value if self.next else None)


if __name__ == '__main__':
    linked_list = LinkedList() \
        .add('a') \
        .add('b') \
        .add('c')

    assert linked_list.get_from_the_end(0) == 'c'
    assert linked_list.get_from_the_end(1) == 'b'
    assert linked_list.get_from_the_end(2) == 'a'
    assert linked_list.get_from_the_end(3) is None
    assert LinkedList().get_from_the_end(0) is None

    assert get_from_the_end_recursive(linked_list.head, 0) == 'c'
    assert get_from_the_end_recursive(linked_list.head, 1) == 'b'
    assert get_from_the_end_recursive(linked_list.head, 2) == 'a'
    assert get_from_the_end_recursive(linked_list.head, 3) is None
    assert get_from_the_end_recursive(None, 3) is None

    linked_list = LinkedList() \
        .add('a') \
        .add('b') \
        .add('c') \
        .add('d') \
        .add('e') \
        .add('f') \
        .add('g') \
        .add('h') \
        .add('i') \
        .add('j') \
        .add('k')

    assert linked_list.get_from_the_end(3) == 'h'
    assert linked_list.get_from_the_end(6) == 'e'
    assert linked_list.get_from_the_end(10) == 'a'
    assert linked_list.get_from_the_end(11) is None
