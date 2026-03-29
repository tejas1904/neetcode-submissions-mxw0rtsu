import functools
class Solution:
    def rob(self, nums: List[int]) -> int:

        for i in range(len(nums)-1-2,-1,-1):
            nums[i] = max(nums[i]+nums[i+2] , nums[i+1])
        
        return max(nums)