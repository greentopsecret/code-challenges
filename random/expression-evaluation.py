def evaluate(expr):
    operands_stack = []
    operators_stack = []
    for token in expr:
        if token == ' ':
            continue
        if token in '+-/*()':
            operators_stack.append(token)
        elif token.isdigit():
            operands_stack.append(token)
        # elif char in '()':
        #     continue

    while len(operands_stack):
        operand = operands_stack.pop()
        if operand == '':
            pass


if __name__ == '__main__':
    assert evaluate("10 + 2 * 6") == 120
    assert evaluate("100 * 2 + 12") == 212
    assert evaluate("100 * ( 2 + 12 )") == 1400
    assert evaluate("100 * ( 2 + 12 ) / 14") == 100
    assert evaluate("100 * (( 2 + 12 ) - 7)") == 700
    assert evaluate("((100 * ( 4 + 12 )) * (3 + 4)) / 7") == 1600
