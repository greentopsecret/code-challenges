from bisect import bisect_left


def solution(arr: list) -> list:
	true_indexes = set()
	for query, idx in arr:
		if query == 1:  # set
			true_indexes.add(idx)

	true_indexes = sorted(list(true_indexes))

	result = []
	for query, idx in arr:
		if query == 2:  # get
			r = bisect_left(true_indexes, idx)
			if r == len(true_indexes):
				result.append(-1)
			else:
				result.append(true_indexes[r])

	return result


if __name__ == '__main__':
	def main():
		i = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
		assert solution(i) == [-1, 2, -1, 2], print(solution(i))

		print('All tests are passed')


	main()
