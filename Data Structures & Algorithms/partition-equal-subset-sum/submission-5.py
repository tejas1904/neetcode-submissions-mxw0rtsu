class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        target = sum(nums)//2


        dp  =[[False]*(target+1) for _ in range(len(nums))]

        #filling in first row
        for trgt in range(target+1):
            if nums[0]==target:
                dp[0][trgt] = True
        #filling first col
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1,len(nums)):
            for trgt in range(1, target+1 ):
                if nums[i]<=trgt:
                    dp[i][trgt] = (
                        dp[i-1][trgt - nums[i]]
                        or
                        dp[i-1][trgt]
                    )
                else:
                    dp[i][trgt]  = dp[i-1][trgt]
        
        return dp[len(nums)-1][target]


        