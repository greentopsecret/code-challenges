def solution(grid: list[list[int]]) -> int:
    return UniquePaths(grid).solution()


class UniquePaths:
    """
    https://leetcode.com/problems/unique-paths-iii/discuss/221946/JavaPython-Brute-Force-Backtracking
    """

    def __init__(self, grid: list[list[int]]):
        self.res = 0
        self.m = 0
        self.n = 0
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])

    def solution(self):
        r, c = 0, 0
        empty = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    r, c = (i, j)
                elif self.grid[i][j] == 0:
                    empty += 1

        self.dfs(r, c, empty + 1)
        return self.res

    def dfs(self, r, c, empty):
        if not (0 <= r < self.m and 0 <= c < self.n and self.grid[r][c] >= 0):
            return
        if self.grid[r][c] == 2:
            self.res += empty == 0
            return
        self.grid[r][c] = -2
        self.dfs(r + 1, c, empty - 1)
        self.dfs(r - 1, c, empty - 1)
        self.dfs(r, c + 1, empty - 1)
        self.dfs(r, c - 1, empty - 1)
        self.grid[r][c] = 0


if __name__ == '__main__':
    def main():
        grid = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, -1]
        ]
        assert solution(grid) == 2

        grid = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2]
        ]
        assert solution(grid) == 4

        grid = [
            [0, 1],
            [2, 0]
        ]
        assert solution(grid) == 0

        grid = [
            [2, 1],
            [0, 0],
        ]
        assert solution(grid) == 0

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
