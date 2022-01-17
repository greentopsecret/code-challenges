def solution(s: str) -> int:
    # return solution_a(s)
    return solution_b(s)


def solution_b(s: str) -> int:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if s[i:j] == s[j - 1:i - 1:-1]:
                return j
            if s[i + 1:j + 1] == s[j:i:-1]:
                return i
            return -1
        i += 1
        j -= 1

    return -1


def solution_a(s: str) -> int:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1

    if i >= j:
        return -1  # input string is a palindrome

    if is_palindrome(s[i:j]):
        return j

    if is_palindrome(s[i + 1:j + 1]):
        return i

    return -1


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


if __name__ == '__main__':
    def main():
        assert solution('abcfdefggfedcba') == 3
        assert solution('abcfdefgfedcba') == 3
        assert solution('abcdefggfedfcba') == 11
        assert solution('abcdefgfedfcba') == 10

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
