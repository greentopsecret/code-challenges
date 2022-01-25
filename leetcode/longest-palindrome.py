def solution(s: str) -> str:
    """
    https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
    :param s:
    :return:
    """
    res = ""
    for i in range(len(s)):
        # r = l
        # while r < len(s) and s[l] == s[r]:
        #     r += 1
        # res = max(helper(s, l, r - 1), res, key=len)
        res = max(helper(s, i, i), helper(s, i, i + 1), res, key=len)
        # odd case, like "aba"
        # tmp = helper(s, i, i)
        # if len(tmp) > len(res):
        #     res = tmp
        # # even case, like "abba"
        # tmp = helper(s, i, i + 1)
        # if len(tmp) > len(res):
        #     res = tmp
    return res


def helper(s, l, r) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


if __name__ == '__main__':
    def main():
        assert solution("abcdefeduuu") == 'defed'
        assert solution("abcdeffeduuu") == 'deffed'

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
