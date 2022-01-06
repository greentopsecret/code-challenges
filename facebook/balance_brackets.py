# {{[[(())]]}}
# {{[[(())]]}}
def isBalanced(s):
    pairs = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in '}])':
            if len(stack) == 0:
                return False
            p = stack.pop()
            if not p in pairs.keys() or char != pairs[p]:
                return False

    return len(stack) == 0


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    check(False, isBalanced("{[(])}"))
    check(True, isBalanced("{}()"))
    check(False, isBalanced("{(})}"))
    check(False, isBalanced(")"))
    check(False, isBalanced("["))
    check(True, isBalanced("{{[[(())]]}}"))

    # Add your own test cases here
