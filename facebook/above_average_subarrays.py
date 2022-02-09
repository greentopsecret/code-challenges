def solution(arr: list) -> list:
	total_cnt = len(arr)
	total_sum = sum(arr)

	result = []
	for left in range(len(arr)):
		part1_sum = 0
		part2_sum = total_sum
		for right in range(left, len(arr)):
			part1_sum += arr[right]
			part1_cnt = right - left + 1
			part2_sum -= arr[right]
			part2_cnt = total_cnt - part1_cnt
			part1_avg = part1_sum / part1_cnt
			part2_avg = part2_sum / part2_cnt if part2_cnt > 0 else 0
			if part1_avg > part2_avg:
				result.append([left + 1, right + 1])

	return result


if __name__ == '__main__':
	def main():
		assert solution([3, 4, 2]) == [[1, 2], [1, 3], [2, 2]], print(solution([3, 4, 2]))
		assert solution([0]) == [], print(solution([0]))

		print('All tests are passed')


	main()
