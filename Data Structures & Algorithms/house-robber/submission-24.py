import functools


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def rob(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            else:
                memo[i] = max(nums[i] + rob(i + 2), rob(i + 1))
                return memo[i]

        return rob(0)
