import math


def flip_to_win(num: int) -> int:
    sequences = []
    sequence = 0
    while num > 0:
        bit = num % 2
        num = math.floor(num / 2)
        if bit:
            sequence += 1
        else:
            sequences.append(sequence)
            sequence = 0
    sequences.append(sequence)

    max_len = sequences[0]
    for i, _ in enumerate(sequences):
        if i > 0:
            max_len = max(max_len, sequences[i - 1] + sequences[i] + 1)

    return max_len


if __name__ == '__main__':
    def main():
        assert flip_to_win(1775) == 8  # 11011101111
        assert flip_to_win(3535) == 6  # 110111001111
        assert flip_to_win(15) == 4  # 1111

        print('All tests are passed')


    main()
