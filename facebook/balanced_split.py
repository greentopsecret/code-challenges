import math
from heapq import heapify, heappush, heappop


def balancedSplitExists(arr):
	arr = sorted(arr)

	total_sum = sum(arr)
	if total_sum % 2 == 1:
		return False

	small_part_sum = 0
	large_part_sum = total_sum
	for i in range(1, len(arr)):
		num = arr[i - 1]
		small_part_sum += num
		large_part_sum -= num
		if small_part_sum == large_part_sum and num < arr[i]:
			return True

	return False


#  # same time complexity as above but using MinHeap
#  heapify(arr)
#
#  small_part_sum = 0
#  large_part_sum = sum(arr)
#
#  while arr:
#    num = heappop(arr)
#    small_part_sum += num
#    large_part_sum -= num
#    if small_part_sum == large_part_sum and arr and num < arr[0]:
#      return True
#  
#  return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
	print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printString(expected)
		print(' Your output: ', end='')
		printString(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	arr_1 = [2, 1, 2, 5]
	expected_1 = True
	output_1 = balancedSplitExists(arr_1)
	check(expected_1, output_1)

	arr_2 = [3, 6, 3, 4, 4]
	expected_2 = False
	output_2 = balancedSplitExists(arr_2)
	check(expected_2, output_2)

	check(False, balancedSplitExists([12, 7, 6, 7, 6]))

	check(True, balancedSplitExists([1, 5, 7, 1]))

	check(False, balancedSplitExists([]))

	check(False, balancedSplitExists([0]))
