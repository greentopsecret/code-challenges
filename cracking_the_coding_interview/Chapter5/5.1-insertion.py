def insertion(n: int, m: int, i: int, j: int) -> int:
    # mask = (~0 << (j + 1)) | ((1 << i) - 1)
    # return (n & mask) | (m << i)
    all_ones = ~0
    left = all_ones << (j + 1)
    right = ((1 << i) - 1)
    mask = left | right
    n_cleared = n & mask
    m_shifted = m << i

    return n_cleared | m_shifted


if __name__ == '__main__':
    def main():
        assert '{0:b}'.format(insertion(int('100000000000', 2), int('10011', 2), 2, 6)) == '100001001100'
        assert '{0:b}'.format(insertion(int('100001010000', 2), int('10011', 2), 2, 6)) == '100001001100'

        print('All tests are passed')


    main()
