class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def fn(total,i):

            if i==len(nums) and total==target:
                return 1
            elif i==len(nums) and total!=target:
                return 0
            
            return fn(total+nums[i] , i+1)  + fn(total-nums[i] , i+1)
        
        return fn(0,0)
