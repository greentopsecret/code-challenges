class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    def is_even(self):
        return self.data % 2 == 0

    def __str__(self):
        return str(self.data)


# quite ugly solution :/
def reverse_solution_a(head):
    current = head

    # all prefixes represent positions before reversing
    first_even = None
    last_odd = None
    prev = None
    while current:

        _next = current.next

        if current.is_even():
            if prev and prev.is_even():
                current.next = prev
            else:
                first_even = current
                first_even.next = None

            if last_odd:
                last_odd.next = current
            else:
                head = current
        else:
            last_odd = current
            if prev and prev.is_even():
                first_even.next = current

        prev = current
        current = _next

    return head


def reverse_solution_b(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    while current:
        if current.is_even():
            event_part_head, even_part_tail = _reverse_even_part(current)
            prev.next = event_part_head
            prev = even_part_tail
            current = even_part_tail.next
        else:
            prev = current
            current = current.next

    return dummy.next


def _reverse_even_part(head: Node):
    prev = None
    current = head
    tail_after = head
    while current and current.is_even():
        next_node = current.next

        current.next = prev

        prev = current
        current = next_node
        tail_after.next = next_node

    head_after = prev

    return head_after, tail_after


def print_linked_list(head):
    p = ['[']
    while head is not None:
        p.append(head.data)
        head = head.next
        if head is not None:
            p.append(' ')
    p.append(']')
    print(''.join(p))


test_case_number = 1


def check(expected_head, output_head):
    global test_case_number
    temp_expected_head = expected_head
    temp_output_head = output_head
    result = True
    while expected_head is not None and output_head is not None:
        result &= (expected_head.data == output_head.data)
        expected_head = expected_head.next
        output_head = output_head.next

    if not (output_head is None and expected_head is None):
        result = False

    right_tick = '\u2713'
    wrong_tick = '\u2717'
    if result:
        print(right_tick, ' Test #', test_case_number, sep='')
    else:
        print(wrong_tick, ' Test #', test_case_number, ': Expected ', sep='', end='')
        print_linked_list(temp_expected_head)
        print(' Your output: ', end='')
        print_linked_list(temp_output_head)
        print()
    test_case_number += 1


def create_linked_list(arr):
    root = node = None
    for v in arr:
        if root is None:
            node = Node(v)
            root = node
        else:
            node.next = Node(v)
            node = node.next
    return root


if __name__ == "__main__":
    expected_list = create_linked_list([1, 8, 2, 9, 16, 12])
    input_list = create_linked_list([1, 2, 8, 9, 12, 16])
    check(expected_list, reverse_solution_a(input_list))
    input_list = create_linked_list([1, 2, 8, 9, 12, 16])
    check(expected_list, reverse_solution_b(input_list))

    expected_list = create_linked_list([24, 18, 2, 3, 5, 7, 9, 12, 6])
    input_list = create_linked_list([2, 18, 24, 3, 5, 7, 9, 6, 12])
    check(expected_list, reverse_solution_a(input_list))
    input_list = create_linked_list([2, 18, 24, 3, 5, 7, 9, 6, 12])
    check(expected_list, reverse_solution_b(input_list))
