import math
from heapq import heapify, heappush, heappop


def balancedSplitExists(arr):
	# return balanced_split_exists_sort(arr)
	return balanced_split_exists_quickselect(arr)


def can_split(cur_arr, total_lo_sum, target):
	if not cur_arr:
		return False
	pivot = cur_arr[0]
	local_lo_sum, lo, hi = 0, [], []
	for x in cur_arr:
		if x < pivot:
			local_lo_sum += x
			lo.append(x)
		elif x == pivot:
			local_lo_sum += x
		else:
			hi.append(x)
	if target == local_lo_sum + total_lo_sum:
		return True
	elif local_lo_sum + total_lo_sum < target:
		return can_split(hi, local_lo_sum + total_lo_sum, target)
	else:
		return can_split(lo, total_lo_sum, target)


def balanced_split_exists_quickselect(arr):
	if not arr or len(arr) == 1:
		return False
	target = sum(arr)
	if target % 2 != 0:
		return False
	target /= 2

	return can_split(arr, 0, target)


# return balanced_split_exists_quickselect_rec(arr, 0, len(arr) - 1, 0, sum(arr))


def partition(arr, lo, hi):
	left_subpart_sum = 0
	pivot = arr[math.floor((lo + hi) / 2)]
	while lo < hi:
		while arr[lo] < pivot:
			left_subpart_sum += arr[lo]
			lo += 1

		while arr[hi] > pivot:
			hi -= 1

		if lo < hi:
			arr[lo], arr[hi] = arr[hi], arr[lo]
			left_subpart_sum += arr[lo]
			lo += 1
			hi -= 1

	return lo, left_subpart_sum


def balanced_split_exists_quickselect_rec(arr, lo, hi, left_sum, right_sum):
	pivot, left_subpart_sum = partition(arr, lo, hi)
	if left_sum + left_subpart_sum > right_sum - left_subpart_sum:
		return balanced_split_exists_quickselect_rec(
			arr,
			lo,
			pivot - 1,
			left_sum + left_subpart_sum,
			right_sum - left_subpart_sum
		)

	if left_sum + left_subpart_sum < right_sum - left_subpart_sum:
		return balanced_split_exists_quickselect_rec(
			arr,
			pivot,
			hi,
			left_sum + left_subpart_sum,
			right_sum - left_subpart_sum
		)

	if left_sum + left_subpart_sum == right_sum - left_subpart_sum:
		return True


def balanced_split_exists_sort(arr):
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

	check(True, balancedSplitExists([1, 5, 7, 1]))

	check(False, balancedSplitExists([8, 7, 6, 7, 6, 4, 12, 1, 3, 4]))

	arr_1 = [2, 1, 2, 5]
	expected_1 = True
	output_1 = balancedSplitExists(arr_1)
	check(expected_1, output_1)

	arr_2 = [3, 6, 3, 4, 4]
	expected_2 = False
	output_2 = balancedSplitExists(arr_2)
	check(expected_2, output_2)

	check(False, balancedSplitExists([12, 7, 6, 7, 6]))

	check(False, balancedSplitExists([]))

	check(False, balancedSplitExists([0]))
