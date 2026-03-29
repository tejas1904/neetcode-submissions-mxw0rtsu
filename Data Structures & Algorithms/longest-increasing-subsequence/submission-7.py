import functools
class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(prev: int, i: int) -> int:
            if i == n:
                return 0

            # skip nums[i]
            exclude = dfs(prev, i + 1)

            # take nums[i] if valid
            include = 0
            if prev == -1 or nums[prev] < nums[i]:
                include = 1 + dfs(i, i + 1)

            return max(include, exclude)

        return dfs(-1, 0)