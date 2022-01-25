def solution(petrolpumps):
    return solution_a(petrolpumps)
    # return solution_b(petrolpumps)


def solution_a(petrolpumps):
    n = len(petrolpumps)
    for i in range(n):
        j = i
        tank_leftovers = 0
        cnt = 0
        while cnt < n:
            amount, distance = petrolpumps[j]
            tank_leftovers += (amount - distance)
            j += 1
            j %= n
            if tank_leftovers < 0:
                break
            cnt += 1
        if j == i:
            return i
    return -1


def solution_b(petrolpumps):
    diff = 0
    s = 0
    start = 0
    n = len(petrolpumps)
    for i in range(n):
        amount, distance = petrolpumps[i]
        s += amount - distance
        if s < 0:
            start = i + 1
            diff += s
            s = 0

    return start if s + diff >= 0 else -1


if __name__ == '__main__':
    def main():
        # petrolpumps = [
        #     [1, 5],
        #     [10, 3],
        #     [3, 4]
        # ]
        # assert solution(petrolpumps) == 1

        petrolpumps = [
            [4, 3],  # 1
            [3, 2],  # 1
            [3, 6],  # -3
            [2, 1],  # 1
            [2, 2],  # 0
        ]
        assert solution(petrolpumps) == 3

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
