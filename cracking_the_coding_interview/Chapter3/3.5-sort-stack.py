class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[len(self.values) - 1] if len(self.values) else None

    def is_empty(self):
        return len(self.values) == 0

    def sort(self):
        r = Stack()
        while not self.is_empty():
            tmp = self.pop()
            while not r.is_empty() and r.peek() > tmp:
                self.push(r.pop())
            r.push(tmp)

        while not r.is_empty():
            self.push(r.pop())


if __name__ == '__main__':
    stack = Stack()
    stack.push(6)
    stack.push(1)
    stack.push(0)
    stack.push(3)
    stack.push(4)

    assert stack.peek() == 4
    assert stack.pop() == 4
    assert stack.pop() == 3

    stack.push(3)
    stack.push(4)

    stack.sort()

    assert stack.peek() == 0
    assert stack.pop() == 0
    assert stack.pop() == 1
    assert stack.pop() == 3
    assert stack.pop() == 4
    assert stack.pop() == 6

    print('All tests are passed')
