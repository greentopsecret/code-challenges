from collections import Counter
import math


def min_window_alt(s, t):  # easier to follow
    """
    solution from https://leetcode.com/discuss/interview-question/1045207/facebook-online-minimum-length-substrings
    :param s:
    :param t:
    :return:
    """
    res = math.inf
    l, r = 0, 0
    d = Counter(t)
    l_d = 0
    while r < len(s):
        d[s[r]] -= 1
        if d[s[r]] >= 0:
            l_d += 1
        while l_d == len(t):
            res = min(res, r - l + 1)
            d[s[l]] += 1
            if d[s[l]] > 0:
                l_d -= 1
            l += 1
        r += 1
    return res if res != math.inf else -1


# s=dcbefedce
# t=fd
def min_length_substring(s, t):
    if not len(s) or not len(t):
        return False

    counter = Counter(t)

    l = 0
    sub_l = 0
    ml = math.inf
    for r in range(len(s)):
        char = s[r]
        counter[char] -= 1
        if counter[char] >= 0:
            sub_l += 1

        while l <= r and sub_l == len(t):
            ml = min(ml, r - l + 1)
            counter[s[l]] += 1
            if counter[s[l]] > 0:
                sub_l -= 1
            l += 1

    return -1 if ml == math.inf else ml


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    check(3, min_length_substring("dddcbefedce", "fd"))
    check(3, min_window_alt("dddcbefedce", "fd"))
    check(3, min_length_substring("dcbefedce", "fd"))
    check(7, min_length_substring("dcbefedce", "dfd"))
