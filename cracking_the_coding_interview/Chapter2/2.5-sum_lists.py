from LinkedList import LinkedList, Node


def sum_lists(a, b):
    carry = 0
    head = None
    tail = None
    while True:
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


def sum_reverse_lists(ll1: Node, ll2: Node) -> Node:
    # Pad short list with zeros
    len_a = len(ll1)
    len_b = len(ll2)
    if len(ll1) < len(ll2):
        short = ll1
        long = ll2
        r = len_b - len_a
    else:
        long = ll1
        short = ll2
        r = len_a - len_b
    for _ in range(r):
        short = Node(0, next_node=short)

    # calculate sum recursively
    ll, carry = _sum_reverse_lists_recursive(short, long)
    if carry:
        ll = Node(carry, next_node=ll)

    return ll


def _sum_reverse_lists_recursive(ll1: Node, ll2: Node) -> tuple[Node, int]:
    if ll1.next is None and ll2.next is None:
        value = ll1.value + ll2.value
        return Node(value % 10), 1 if value > 9 else 0

    node, carry = _sum_reverse_lists_recursive(ll1.next, ll2.next)
    value = ll1.value + ll2.value + carry
    return Node(value % 10, next_node=node), 1 if value > 9 else 0


if __name__ == '__main__':
    # head617 = Node(7)
    # head617.next = Node(1)
    # head617.next.next = Node(6)
    #
    # head295 = Node(5)
    # head295.next = Node(9)
    # head295.next.next = Node(2)
    #
    # result = sum_lists(head617, head295)
    #
    # head912 = Node(2)
    # head912.next = Node(1)
    # head912.next.next = Node(9)
    #
    # assert str(LinkedList().add(result)) == str(LinkedList().add(head912))

    linked_list_1 = LinkedList([1, 2, 4, 6])
    linked_list_2 = LinkedList([5, 6])

    assert sum_reverse_lists(linked_list_1.head, linked_list_2.head).print_list() == '1 -> 3 -> 0 -> 2'

    linked_list_1 = LinkedList([1, 2, 4, 6])
    linked_list_2 = LinkedList([9, 9, 9, 9])

    assert sum_reverse_lists(linked_list_1.head, linked_list_2.head).print_list() == '1 -> 1 -> 2 -> 4 -> 5'
