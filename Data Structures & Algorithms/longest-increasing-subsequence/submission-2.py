class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp =  [0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            j=i+1
            while j<len(nums):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i],dp[j])
                j+=1
            dp[i] = 1+dp[i]
        
        return max(dp)


        