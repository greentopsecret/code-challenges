import re


def evaluate(expr):
    operands_stack = []
    operators_stack = []
    p = '(\d{1,}|[\+\-\*\/\(\)])'
    for match in re.finditer(p, expr):
        token = match.group()
        if token in '+-/*':
            operators_stack.append(token)
        elif token.isdigit():
            operands_stack.append(token)
        if token in '(':
            continue
        elif token in ')':
            operator = operators_stack.pop()
            if operator == '(':
                break
            operand2 = operands_stack.pop()
            operand1 = operands_stack.pop()
            operands_stack.append(eval('%s %s %s' % (operand1, operator, operand2)))

    while len(operands_stack) > 1:
        operand2 = operands_stack.pop()
        operand1 = operands_stack.pop()
        operator = operators_stack.pop()
        operands_stack.append(eval('%s %s %s' % (operand1, operator, operand2)))

    return operands_stack.pop()


if __name__ == '__main__':
    def main():
        assert evaluate("10 + ((2 + 6) * 2)") == 26
        assert evaluate("10 + (2 * 6)") == 22
        assert evaluate("(100 * 2) + 12") == 212
        assert evaluate("100 * ( 2 + 12 )") == 1400
        assert evaluate("100 * ( 2 + 12 ) / 14") == 100
        assert evaluate("100 * (( 2 + 12 ) - 7)") == 700
        assert evaluate("((100 * ( 4 + 12 )) * (3 + 4)) / 7") == 1600

        print('All tests are passed')

    main()
