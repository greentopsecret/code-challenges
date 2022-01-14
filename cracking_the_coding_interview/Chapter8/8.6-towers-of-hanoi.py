from collections import deque

class Tower:
    def __init__(self):
        self.disks = deque()

    def append(self, disk: int):
        if len(self.disks) > 0 and disk > self.disks[-1]:
            raise Exception('Wrong order - you cannot put %d on top of %d' % (disk, self.disks[-1]))

        self.disks.append(disk)

    def pop(self) -> int:
        return self.disks.pop()

    def __len__(self):
        return len(self.disks)

    def __str__(self):
        return str(self.disks)


def solution(size: int):
    origin = Tower()
    destination = Tower()
    buffer = Tower()

    # init stack 1
    for i in range(size, 0, -1):
        origin.append(i)

    print('Original stack - BEFORE: %s' % origin)
    print('Destination stack - BEFORE: %s' % destination)
    print('Buffer stack - BEFORE: %s' % buffer)
    print()

    solution_recursive(origin, destination, buffer)

    print('Original stack - AFTER: %s' % origin)
    print('Destination stack - AFTER: %s' % destination)
    print('Buffer stack - AFTER: %s' % buffer)
    print()


def solution_recursive(origin: Tower, destination: Tower, buffer: Tower):
    move_disks(len(origin), origin, destination, buffer)


def move_disks(n: int, origin: Tower, destination: Tower, buffer: Tower):
    if n == 0:
        return

    move_disks(n - 1, origin, buffer, destination)

    destination.append(origin.pop())

    move_disks(n - 1, buffer, destination, origin)


if __name__ == '__main__':
    def main():

        solution(5)

        print('All tests are passed')


    main()
