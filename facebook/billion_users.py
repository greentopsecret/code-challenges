import math


def get_billion_users_day(growth_rates):
	target = 1e9
	left = 0
	right = math.ceil(math.log(target, min(growth_rates)))
	while left < right:
		mid = math.floor((left + right) / 2)

		total = 0
		for rate in growth_rates:
			total += rate ** mid

		if total > target:
			right = mid
		elif total < target:
			left = mid + 1
		else:
			return mid

	return right if right > 0 else -1


def get_billion_users_day2(growth_rates):
	target = 1e9
	g = max(growth_rates)
	l = 0
	h = math.ceil(math.log(target, g))
	while l < h:
		mid = math.floor((l + h) / 2)
		if g ** mid > target:
			h = mid
		elif g ** mid < target:
			l = mid + 1
		else:
			return mid

	return h


def get_billion_users_day_bruteforce2(growth_rates):
	target = 1e9
	current = 0
	days_cnt = 0
	g = max(growth_rates)
	while current < target:
		current = g ** days_cnt
		days_cnt += 1

	return days_cnt


def get_billion_users_day_bruteforce1(growth_rates):
	target = 1e9
	current = 0
	days_cnt = 0
	users_per_app = [0 for _ in growth_rates]
	while current < target:

		current = 0
		for idx, cnt in enumerate(users_per_app):
			users_per_app[idx] = users_per_app[idx] * growth_rates[idx] if users_per_app[idx] > 0 else growth_rates[idx]
			current += users_per_app[idx]

		days_cnt += 1

	return days_cnt


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
	print('[', n, ']', sep='', end='')


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
		printInteger(expected)
		print(' Your output: ', end='')
		printInteger(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	check(9, get_billion_users_day([10]))

	check(8, get_billion_users_day([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

	test_1 = [1.1, 1.2, 1.3]
	expected_1 = 79
	output_1 = get_billion_users_day(test_1)
	check(expected_1, output_1)

	test_2 = [1.01, 1.02]
	expected_2 = 1047
	output_2 = get_billion_users_day(test_2)
	check(expected_2, output_2)

	check(52, get_billion_users_day([1.5]))

	check(-1, get_billion_users_day([0.9]))

	check(-1, get_billion_users_day([0.1, 1.1]))

	check(1, get_billion_users_day([1e9]))
