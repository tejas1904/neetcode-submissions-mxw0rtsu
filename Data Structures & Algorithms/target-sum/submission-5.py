class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo =  {}
        def bktrak(i,currsum):
            if (i,currsum) in memo:
                return memo[(i,currsum)]
            if i == len(nums):
                if currsum==target:
                    return 1
                else:
                    return 0
            else:
                memo[(i,currsum)] = bktrak(i+1,currsum+nums[i]) + bktrak(i+1,currsum-nums[i])
                return memo[(i,currsum)]
        
        return bktrak(0,0)