from collections import defaultdict


# s=dcbefedce
# t=fd
def min_length_substring(s, t):
    if not len(s) or not len(t):
        return False

    freq = defaultdict(int)
    for char in t:
        freq[char] += 1

    l = 0
    ml = 1000001
    for r in range(len(s)):
        char = s[r]
        if char in freq.keys():
            freq[char] -= 1

        while l <= r and max(freq.values()) == 0:
            ml = min(ml, r - l + 1)
            if s[l] in freq.keys():
                freq[s[l]] += 1
            l += 1

    return -1 if ml == 1000001 else ml


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

    check(3, min_length_substring("dcbefedce", "fd"))
    check(7, min_length_substring("dcbefedce", "dfd"))

    # Add your own test cases here
