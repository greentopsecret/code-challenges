from os.path import realpath, dirname
from collections import deque


def solution(s: str) -> str:
    if len(s) % 2 != 0:
        return 'NO'

    stack = deque()
    pairs = {
        ']': '[',
        ')': '(',
        '}': '{',
    }
    for symb in s:
        if symb in ['{', '(', '[']:
            stack.append(symb)
            continue
        if len(stack) == 0 or stack.pop() != pairs.get(symb):
            return 'NO'

    return 'YES' if len(stack) == 0 else 'NO'


def run_tests(input_file_name: str, output_file_name: str):
    f_input = open(input_file_name, mode='r')
    f_output = open(output_file_name, mode='r')
    cnt = int(f_input.readline())
    while cnt > 0:
        l_input = f_input.readline().strip()
        expected_output = f_output.readline().strip()
        if not l_input or not expected_output:
            break
        actual_output = solution(l_input)
        if actual_output != expected_output:
            print(':/')
        assert actual_output == expected_output
        cnt -= 1


def main():
    _dir = dirname(realpath(__file__))

    input_file_name = _dir + '/input/balanced-brackets/input.txt'
    output_file_name = _dir + '/input/balanced-brackets/output.txt'
    run_tests(input_file_name, output_file_name)

    input_file_name = _dir + '/input/balanced-brackets/input-4.txt'
    output_file_name = _dir + '/input/balanced-brackets/output-4.txt'
    run_tests(input_file_name, output_file_name)

    input_file_name = _dir + '/input/balanced-brackets/input-5.txt'
    output_file_name = _dir + '/input/balanced-brackets/output-5.txt'
    run_tests(input_file_name, output_file_name)

    input_file_name = _dir + '/input/balanced-brackets/input-9.txt'
    output_file_name = _dir + '/input/balanced-brackets/output-9.txt'
    run_tests(input_file_name, output_file_name)

    # print(solution([1, 2, 3]))

    print('All tests are passed')


if __name__ == '__main__':
    main()
