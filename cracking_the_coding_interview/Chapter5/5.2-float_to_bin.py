import math
from collections import deque


def float_to_bin(f: float):
    num = int(f)
    result = deque()
    div = 2
    if num > 0:
        while num > 0:
            result.appendleft(str(num % div))
            num = math.floor(num / div)
    else:
        result.append('0')

    num = f - int(f)
    fraction = 1 / 2
    if num > 0:
        result.append('.')
        while num > 0:
            if len(result) >= 64:
                return 'ERROR'
            if num >= fraction:
                result.append('1')
                num -= fraction
            else:
                result.append('0')
            fraction /= 2

    return ''.join(result)


if __name__ == '__main__':
    def main():
        for var in [0.893, 0.4, 0.5, 1.5, 0.25, 0.75, 0.875, 0.625, 0.375, 0.2578125]:
            print('%s => %s' % (var, float_to_bin(var)))


    main()
