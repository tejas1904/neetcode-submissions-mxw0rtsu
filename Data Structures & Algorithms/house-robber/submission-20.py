import functools
class Solution:
    def rob(self, nums: List[int]) -> int:

        @functools.lru_cache(None)
        def bktrak(i):
            if i>=len(nums):
                return 0
            else:
                return max(nums[i]+bktrak(i+2),bktrak(i+1))
        return bktrak(0)
        