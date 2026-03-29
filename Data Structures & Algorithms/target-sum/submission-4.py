class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def bktrak(i,currsum):
            if i == len(nums):
                if currsum==target:
                    return 1
                else:
                    return 0
            else:
                return bktrak(i+1,currsum+nums[i]) + bktrak(i+1,currsum-nums[i])
        
        return bktrak(0,0)
