from collections import deque


def solution_bfs(arr):
	current = ''.join([str(x) for x in arr])
	target = ''.join([str(x) for x in sorted(arr)])

	queue1 = deque()
	queue1.appendleft((current, 0))
	queue2 = deque()
	queue2.appendleft((target, 0))
	visited1 = {current: 0}
	visited2 = {target: 0}

	while len(queue1) and len(queue2):
		item1, swap_cnt1 = queue1.pop()
		if item1 in visited2.keys():
			return visited2[item1] + swap_cnt1

		for left in range(0, len(arr)):
			for right in range(left + 1, len(arr) + 1):
				item = item1[:left] + item1[left:right][::-1] + item1[right:]
				if item not in visited1:
					queue1.appendleft((item, swap_cnt1 + 1))
					visited1[item] = swap_cnt1 + 1

		item2, swap_cnt2 = queue2.pop()
		if item2 in visited1.keys():
			return visited1[item2] + swap_cnt2

		for left in range(0, len(arr)):
			for right in range(left + 1, len(arr) + 1):
				item = item2[:left] + item2[left:right][::-1] + item2[right:]
				if item not in visited2:
					queue2.appendleft((item, swap_cnt2 + 1))
					visited2[item] = swap_cnt2 + 1

	return -1


def solution(arr: list) -> int:
	return solution_bfs(arr)
	arr_sorted = sorted([x for x in arr])
	indexes = {v: k for k, v in enumerate(arr)}

	swap_cnt = 0
	for idx, value in enumerate(arr):
		n = arr_sorted[idx]
		if n < value:
			reverse_sub_array(arr, idx, indexes[n], indexes)
			swap_cnt += 1

	return swap_cnt


def reverse_sub_array(arr, _min, _max, indices_map):
	i = _min
	j = _max
	# print(f"swap: {{}} {{}}".format(_min, _max))
	while i < j:
		swap(i, j, arr)
		indices_map[arr[i]] = i
		indices_map[arr[j]] = j
		i += 1
		j -= 1


def swap(i, j, arr):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp


def solution_leetcode(arr: list) -> int:
	indices_map = {}
	sorted_copy = sorted([x for x in arr])
	for idx in range(len(arr)):
		indices_map[arr[idx]] = idx

	swap_count = 0
	for idx, char_origin in enumerate(arr):
		char_target = sorted_copy[idx]
		if char_target < char_origin:
			reverse_sub_array(
				arr,
				min(indices_map[char_target], idx),
				max(indices_map[char_target], idx),
				indices_map
			)
			swap_count += 1

	return swap_count


if __name__ == '__main__':
	def main():
		result = solution([3, 1, 2])
		assert result == 2, result

		result = solution([1, 2, 5, 4, 3])
		assert result == 1, result

		result = solution([9, 1, 7, 3, 5, 4, 6, 2, 8, 0])
		# [9, 1, 7, 3, 5, 4, 6, 2, 8, 0]
		# [0, 8, 2, 6, 4, 5, 3, 7, 1, 9]
		# [0, 1, 7, 3, 5, 4, 6, 2, 8, 9]
		# [0, 1, 2, 6, 4, 5, 3, 7, 8, 9]
		# [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
		# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		assert result == 5, result

		result = solution([5, 2, 3, 4, 1])
		assert result == 2, result

		result = solution([5, 4, 3, 2, 1])
		assert result == 1, result

		result = solution([1, 2, 7, 5, 3, 4, 6])
		assert result == 4, result

		print('All tests are passed')


	main()
