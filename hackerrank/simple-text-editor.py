def solution(ops: list) -> int:
    s = ''
    states = []
    for op in ops:
        if op[0] == '1':
            states.append(s)
            s += op[2:]
        if op[0] == '2':
            states.append(s)
            n = int(op[2:])
            s = s[:-n]
        if op[0] == '3':
            n = int(op[2:])
            print(s[n - 1])
        if op[0] == '4':
            s = states.pop()


if __name__ == '__main__':
    def main():
        solution(['1 abc', '3 3', '2 3', '1 xy', '3 2', '4', '4', '3 1'])

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
