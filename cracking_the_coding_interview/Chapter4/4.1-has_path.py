from queue import SimpleQueue
from enum import Enum


class State(Enum):
    UNVISITED = 0
    VISITED = 1
    VISITING = 2


class Node:
    def __init__(self, value):
        self.state = State.UNVISITED
        self.value = value
        self.adjacent = []

    def mark_unvisited(self):
        self.state = State.UNVISITED

    def mark_visited(self):
        self.state = State.VISITED

    def is_visited(self):
        return self.state == State.VISITED

    def add_adjacent(self, node):
        self.adjacent.append(node)
        return self

    def get_adjacent(self):
        return self.adjacent


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def _reset_nodes(self):
        for node in self.nodes:
            node.mark_unvisited()

    def has_path(self, start: Node, end: Node):
        if start == end:
            return True

        self._reset_nodes()

        start.mark_visited()

        queue = SimpleQueue()
        queue.put(start)

        while not queue.empty():
            node = queue.get()

            for n in node.get_adjacent():
                if n.is_visited():
                    continue
                if n == end:
                    return True
                n.mark_visited()
                queue.put(n)

        return False


if __name__ == '__main__':
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    # cluster 1
    n6.add_adjacent(n5)
    n5.add_adjacent(n4)
    n4.add_adjacent(n6)

    # cluster 2
    n0.add_adjacent(n1)
    n1.add_adjacent(n2)
    n2.add_adjacent(n0).add_adjacent(n3)
    n3.add_adjacent(n2).add_adjacent(n7)
    n7.add_adjacent(n8)
    n9.add_adjacent(n7)

    graph = Graph([n0, n1, n2, n3, n4, n5, n6, n7, n8, n9])

    assert graph.has_path(n0, n8)
    assert not graph.has_path(n6, n3)
    assert not graph.has_path(n1, n9)

    print('All tests are passed')
