class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif(len(nums)==1):
            return nums[0]
        elif(len(nums)==2):
            return max(nums)
        else:
            dp = [nums[-2],nums[-1]]
            for i in range(len(nums)-3,-1,-1):
                best = max(nums[i]+dp[1] , dp[0])
                dp[0],dp[1] = best,dp[0]
        
        return max(dp)

        