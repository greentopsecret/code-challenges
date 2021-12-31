# https://leetcode.com/problems/longest-arithmetic-subsequence/

from collections import defaultdict
from typing import List


def longest_arith_seq_length(nums: List[int]) -> int:
    dp = defaultdict()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            x = nums[i]
            y = nums[j]
            d = x - y
            dp[j, d] = dp.get((i, d), 1) + 1

    # for i in range(1, len(nums)):
    #     for j in range(0, i):
    #         x = nums[i]
    #         y = nums[j]
    #         d = x - y
    #         dp[i, d] = dp.get((j, d), 1) + 1
    #         # dp[i, nums[i] - nums[j]] = dp.get((j, nums[i] - nums[j]), 1) + 1

    return max(dp.values())


if __name__ == '__main__':
    assert longest_arith_seq_length([20, 1, 15, 3, 10, 5, 8]) == 4
    assert longest_arith_seq_length([3, 6, 9, 12]) == 4
    assert longest_arith_seq_length([9, 4, 7, 2, 10]) == 3
