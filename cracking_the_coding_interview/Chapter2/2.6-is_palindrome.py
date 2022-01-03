class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __len__(self):
        if self.next is None:
            return 1

        # iterative approach is more optimal in terms of space, but recursive one is less trivial
        return len(self.next) + 1


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        for values in values:
            self.add(values)

    def add(self, value):
        if self.head and self.tail:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(value)

    def __iter__(self):
        if self.head is None:
            return []

        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        cnt = 0
        node = self.head
        while node:
            cnt += 1
            node = node.next

        return cnt


def is_palindrome_solution_a(ll: LinkedList):
    slow = ll.head
    fast = ll.head
    stack = []
    while fast and fast.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    if fast:  # odd number of nodes
        slow = slow.next

    right = slow
    while right:
        left = stack.pop()
        if left.value != right.value:
            return False
        right = right.next

    return True


def is_palindrome_solution_b(ll: LinkedList):
    length = len(ll)
    _, result = _is_palindrome_recursive(ll.head, length)

    return result


def _is_palindrome_recursive(head, length) -> tuple[Node, bool]:
    if length == 1:  # odd number of nodes
        return head.next, True

    if length == 0:  # even number of nodes
        return head, True

    node, result = _is_palindrome_recursive(head.next, length - 2)

    if not result:
        return node, result

    return node.next, node.value == head.value


if __name__ == '__main__':
    assert is_palindrome_solution_a(LinkedList([1, 3, 5, 7, 8, 7, 5, 3, 1]))
    assert is_palindrome_solution_b(LinkedList([1, 3, 5, 7, 8, 7, 5, 3, 1]))

    assert is_palindrome_solution_a(LinkedList([1, 7, 7, 1]))
    assert is_palindrome_solution_b(LinkedList([1, 7, 7, 1]))

    assert not is_palindrome_solution_a(LinkedList([1, 3, 2]))
    assert not is_palindrome_solution_b(LinkedList([1, 3, 2]))

    assert not is_palindrome_solution_a(LinkedList([1, 3, 2, 1]))
    assert not is_palindrome_solution_b(LinkedList([1, 3, 2, 1]))

    print('All tests passed')
