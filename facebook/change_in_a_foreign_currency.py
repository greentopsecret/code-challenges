import math


def can_get_exact_change(target, denominations):
	return can_get_exact_change_cached(target, sorted(denominations), set())


def can_get_exact_change_cached(target, denominations, seen):
	if target in seen:
		return False

	result = can_get_exact_change_rec(target, denominations)

	seen.add(target)

	return result


def can_get_exact_change_rec(target, denominations):
	for den in denominations:
		if den > target:
			return False

		if target % den == 0:
			return True

		if can_get_exact_change(target - den, denominations):
			return True

	return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def print_string(string):
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
		print_string(expected)
		print(' Your output: ', end='')
		print_string(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	target_1 = 94
	arr_1 = [5, 10, 25, 100, 200]
	expected_1 = False
	output_1 = can_get_exact_change(target_1, arr_1)
	check(expected_1, output_1)

	target_2 = 75
	arr_2 = [4, 17, 29]
	expected_2 = True
	output_2 = can_get_exact_change(target_2, arr_2)
	check(expected_2, output_2)

# Add your own test cases here
