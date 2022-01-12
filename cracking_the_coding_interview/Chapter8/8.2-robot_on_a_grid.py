from collections import deque, defaultdict


def solution(maze) -> int:
    return solution_recursive(len(maze[0]) - 1, len(maze) - 1, maze, defaultdict(int))
    # return solution_via_stack(maze)


def solution_via_stack(maze) -> int:
    c = len(maze[0]) - 1
    r = len(maze) - 1

    stack = deque()
    stack.append([c, r])

    cnt = 0
    while len(stack) > 0:
        c, r = stack.pop()
        if c == 0 and r == 0:
            cnt += 1
        if c - 1 >= 0 and maze[r][c - 1]:
            stack.append([c - 1, r])
        if r - 1 >= 0 and maze[r - 1][c]:
            stack.append([c, r - 1])

    return cnt


def solution_recursive(c, r, maze, cache: dict) -> int:
    if c == 0 and r == 0:
        return 1

    if (c, r) not in cache.keys():
        cnt = 0
        if c - 1 >= 0 and maze[r][c - 1]:
            cnt += solution_recursive(c - 1, r, maze, cache)
        if r - 1 >= 0 and maze[r - 1][c]:
            cnt += solution_recursive(c, r - 1, maze, cache)
        cache[(c, r)] = cnt

    return cache[(c, r)]


if __name__ == '__main__':
    def main():
        maze = [
            [True, True],
        ]
        assert solution(maze) == 1

        maze = [
            [True],
            [True],
        ]
        assert solution(maze) == 1

        maze = [
            [True, True, True],
            [True, False, True],
            [True, True, True],
        ]
        assert solution(maze) == 2

        maze = [
            [True, True, True],
            [True, False, False],
            [True, True, True],
        ]
        assert solution(maze) == 1

        maze = [
            [True, True, True],
            [True, True, True],
        ]
        assert solution(maze) == 3

        maze = [
            [True, True, True],
            [True, True, True],
            [True, True, True],
        ]
        assert solution(maze) == 6

        maze = [
            [True, False, True],
            [True, True, True],
            [True, True, True],
        ]
        assert solution(maze) == 3

        maze = [
            [False, False, True],
            [True, True, True],
            [False, True, True],
        ]
        assert solution(maze) == 0

        maze = [
            [True, True, True],
            [True, True, True],
            [True, True, True],
        ]
        solution(maze)

        maze = [
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
        ]
        assert solution(maze) == 20

        maze = [
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
        ]
        assert solution(maze) == 70

        maze = [
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
        ]
        assert solution(maze) == 48620

        maze = [
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True],
        ]
        assert solution(maze) == 705432

        maze = [
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True],
        ]
        assert solution(maze) == 2704156

        print('All tests are passed')


    main()
