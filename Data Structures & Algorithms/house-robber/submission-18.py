class Solution:
    def rob(self, nums: List[int]) -> int:
        n  = len(nums)-1

        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i>n:
                return 0
            else:
                memo[i] =  max(nums[i]+dp(i+2) , dp(i+1))
                return memo[i]
        
        return dp(0)

        