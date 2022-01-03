def rotate(matrix: list[list]):
    if len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first  # from the right/bottom
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return True


if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 3, 0],
        [4, 5, 6, 7, 0],
        [8, 9, 10, 11, 0],
        [12, 13, 14, 15, 0],
        [0, 0, 0, 0, 0],
    ]
    rotate(matrix)
    assert matrix == [
        [0, 12, 8, 4, 0],
        [0, 13, 9, 5, 1],
        [0, 14, 10, 6, 2],
        [0, 15, 11, 7, 3],
        [0, 0, 0, 0, 0],
    ]
    matrix = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
    ]
    rotate(matrix)
    assert matrix == [
        [12, 8, 4, 0],
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
    ]
