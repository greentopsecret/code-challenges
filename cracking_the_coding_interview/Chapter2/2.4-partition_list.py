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

    def partition(self, k):

        if self.head is None:
            return

        current = self.head
        left_part_head = None
        left_part_tail = None
        right_part_head = None
        right_part_tail = None
        while current is not None:
            if current.value < k:
                if left_part_tail:
                    left_part_tail.next = current
                if not left_part_head:
                    left_part_head = current
                left_part_tail = current
            else:
                if right_part_tail:
                    right_part_tail.next = current
                if not right_part_tail:
                    right_part_head = current
                right_part_tail = current
            n = current.next
            current.next = None
            current = n

        if left_part_tail:
            left_part_tail.next = right_part_head

        self.head = left_part_head if left_part_head else right_part_head
        self.tail = right_part_tail if right_part_tail else left_part_tail

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        return ' -> '.join(values)


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return '%s (next=%s)' % (str(self.value), str(self.next.value) if self.next else None)


if __name__ == '__main__':
    linked_list = LinkedList() \
        .add(3) \
        .add(5) \
        .add(8) \
        .add(5) \
        .add(10) \
        .add(2) \
        .add(1)

    # print(str(linked_list))

    linked_list.partition(5)

    # print(str(linked_list))

    assert str(linked_list) == '3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10'
