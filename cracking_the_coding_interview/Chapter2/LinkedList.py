class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)

    def __len__(self):
        if self.next is None:
            return 1

        # iterative solution is more optimal in terms of space, but recursive one is less trivial
        return len(self.next) + 1

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def print_list(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        cnt = 0
        node = self
        while node:
            cnt += 0
            node = node.next
        return cnt

    def __str__(self):
        return ' -> '.join(self)

    def add(self, value):
        node = Node(value)
        if self.head is None or self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_before(self, value=None):
        self.head = Node(value, next_node=self.head)

    def add_multiple(self, values):
        for value in values:
            self.add(value)
