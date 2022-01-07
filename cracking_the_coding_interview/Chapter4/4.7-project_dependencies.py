from collections import defaultdict
from queue import SimpleQueue
from collections import deque
from operator import itemgetter


class Node:
    def __init__(self, value: str):
        self.in_nodes = []
        self.out_nodes = []
        self.value = value

    def add_in_node(self, node):
        self.in_nodes.append(node)

    def add_out_node(self, node):
        self.out_nodes.append(node)

    def get_in_cnt(self):
        return len(self.in_nodes)


class Graph:
    def __init__(self, dependencies: list):
        self.nodes = {}
        for item in dependencies:
            name_out, name_in = item
            node_in = self._get_node(name_in)
            node_out = self._get_node(name_out)
            node_in.add_out_node(node_out)
            node_out.add_in_node(node_in)

    def _get_node(self, name: str) -> Node:
        if name not in self.nodes.keys():
            self.nodes[name] = Node(name)
        return self.nodes[name]

    # def get_ordered(self):
    #     start = None
    #     for node in self.nodes:
    #         if


def organise_projects(projects, deps):
    # return Graph(dependencies).get_ordered()
    in_cnt = defaultdict(int)
    # out_cnt = defaultdict(int)
    out_dependencies = defaultdict(list)
    for item in deps:
        out_project, in_project = item
        in_cnt[in_project] += 1
        out_dependencies[out_project].append(in_project)

    queue = deque()
    for project in projects:
        if in_cnt[project] == 0:
            queue.append(project)

    result = []
    while len(queue) > 0:
        # cnt = len(queue)
        # for _ in range(cnt):
        project = queue.popleft()
        result.append(project)
        for p in out_dependencies[project]:
            in_cnt[p] -= 1
            if in_cnt[p] == 0:
                queue.append(p)

    return result if len(result) == len(projects) else -1


if __name__ == '__main__':
    def main():
        deps = [
            ('a', 'd'),
            ('f', 'b'),
            ('b', 'd'),
            ('f', 'a'),
            ('d', 'c'),
        ]
        assert organise_projects(['a', 'b', 'c', 'd', 'e', 'f'], deps) == ['e', 'f', 'b', 'a', 'd', 'c']

        # # graph with a loop
        # deps = [
        #     ('a', 'd'),
        #     ('f', 'b'),
        #     ('b', 'd'),
        #     ('f', 'a'),
        #     ('d', 'c'),
        #     ('c', 'g'),
        #     ('g', 'b')
        # ]
        # assert organise_projects(['a', 'b', 'c', 'd', 'e', 'f', 'g'], deps) is False

        print('All tests are passed')


    main()
