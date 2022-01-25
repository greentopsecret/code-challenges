#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict
from os.path import dirname, realpath


def bfs(n, m, edges, s):
    graph = {i: set() for i in range(1, n + 1)}
    seen = defaultdict(bool)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    dist = 0
    result = {i: -1 for i in range(1, n + 1) if i != s}
    queue = deque()
    queue.appendleft(s)
    seen[s] = True
    while len(queue):
        _len = len(queue)
        dist += 6
        for _ in range(_len):
            node = queue.pop()
            for n in graph[node]:
                if seen[n]:
                    continue
                seen[n] = True
                queue.appendleft(n)
                result[n] = dist

    return list(result.values())


def run_tests(input_file_name: str, output_file_name: str):
    f_input = open(input_file_name, mode='r')
    f_output = open(output_file_name, mode='r')
    cnt = int(f_input.readline())
    while cnt > 0:
        n, m = map(int, f_input.readline().strip().split(' '))
        edges = []
        while m > 0:
            l_input = f_input.readline().strip()
            edges.append(list(map(int, l_input.split(' '))))
            m -= 1
        start = int(f_input.readline().strip())

        expected_output = list(map(int, f_output.readline().strip().split(' ')))

        actual_output = bfs(n, m, edges, start)
        if actual_output != expected_output:
            print(':/')
        assert actual_output == expected_output
        cnt -= 1


def main():
    assert bfs(5, 3, [[1, 2], [1, 3], [3, 4]], 1) == [6, 6, 12, -1]
    assert bfs(5, 3, [[1, 2], [1, 4], [4, 5]], 1) == [6, -1, 6, 12]

    _dir = dirname(realpath(__file__))

    input_file_name = _dir + '/input/bfs-shortest-reach/input-01.txt'
    output_file_name = _dir + '/input/bfs-shortest-reach/output-01.txt'
    run_tests(input_file_name, output_file_name)

    # print(solution([1, 2, 3]))

    print('All tests are passed')


if __name__ == '__main__':
    main()
