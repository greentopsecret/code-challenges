#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict
from os.path import dirname, realpath

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
WEIGHT = 6


def solution(n, m, edges, s):
    graph = {i: [] for i in range(1, n + 1)}
    visited = defaultdict(bool)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        # graph[edge[1]].append(edge[0])

    dist = 0
    result = {i: -1 for i in range(1, n + 1) if i != s}
    queue = deque()
    queue.appendleft(s)
    while len(queue):
        _len = len(queue)
        dist += WEIGHT
        for _ in range(_len):
            node = queue.pop()
            for n in graph[node]:
                if visited[n]:
                    continue
                visited[n] = True
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

        actual_output = solution(n, m, edges, start)
        if actual_output != expected_output:
            print(':/')
        assert actual_output == expected_output
        cnt -= 1


def main():
    # assert solution(5, 3, [[1, 2], [1, 3], [3, 4]], 1) == [6, 6, 12, -1]
    # assert solution(5, 3, [[1, 2], [1, 4], [4, 5]], 1) == [6, -1, 6, 12]

    _dir = dirname(realpath(__file__))

    input_file_name = _dir + '/input/bfs-shortest-reach/input-01.txt'
    output_file_name = _dir + '/input/bfs-shortest-reach/output-01.txt'
    run_tests(input_file_name, output_file_name)

    # print(solution([1, 2, 3]))

    print('All tests are passed')


if __name__ == '__main__':
    main()
