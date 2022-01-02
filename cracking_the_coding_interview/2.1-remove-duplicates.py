class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def add(self, value):
        self.tail.next = Node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        return self

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return ' -> '.join(values)

    def remove_duplicates(self):
        current = self.tail
        while current is not self.head:
            runner = self.head
            while runner is not None and runner is not current:
                n = runner.next
                if runner.value == current.value:
                    self.remove(runner)
                runner = n
            current = current.prev

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
            if node is self.tail:
                self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
            if node is self.head:
                self.head = node.next


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

    def __str__(self):
        return '%s (prev=%s, next=%s)' % (self.value,
                                          self.prev.value if self.prev else None,
                                          self.next.value if self.next else None)


if __name__ == '__main__':
    linked_list = LinkedList('a') \
        .add('d') \
        .add('e') \
        .add('a') \
        .add('e') \
        .add('f')
    assert str(linked_list) == 'a -> d -> e -> a -> e -> f'
    linked_list.remove_duplicates()
    assert str(linked_list) == 'd -> a -> e -> f'
