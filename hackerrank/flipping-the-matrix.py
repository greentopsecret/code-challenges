def solution(matrix: list[list[int]]) -> int:
    n = int(len(matrix) / 2)
    total = 0
    for r in range(n):
        for c in range(n):
            total += max(
                matrix[r][c],
                matrix[r][2 * n - c - 1],
                matrix[2 * n - r - 1][2 * n - c - 1],
                matrix[2 * n - r - 1][c],
            )

    return total


if __name__ == '__main__':
    def main():
        m = [
            [0, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0, 1],
            [2, 3, 4, 5, 6, 7],
            [8, 9, 0, 1, 2, 3],
            [4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5],
        ]

        assert solution(m) == 60

        m = [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108]
        ]
        assert solution(m) == 414

        print('All tests are passed')


    main()
