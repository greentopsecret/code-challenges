def solution(skills, teamSize, maxDiff) -> int:
    if not skills:
        return 0

    skills = sorted(skills)
    cnt = 0
    i = 0
    while i + teamSize <= len(skills):
        if skills[i + teamSize - 1] - skills[i] <= maxDiff:
            cnt += 1
            i += teamSize
        else:
            i += 1

    return cnt


if __name__ == '__main__':
    def main():
        # assert solution([1, 2, 3, 0, 5]) is None
        assert solution([1, 1, 2, 4, 5, 5], 3, 2) == 2
        # assert solution([6, 5, 1, 2, 1, 4, 5, 3, 2], 3, 2) == 2

        # print(solution([1, 2, 3]))

        print('All tests are passed')


    main()
