import functools
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = 0
        
        for i in range(len(nums)):
            if i<=canReach:
                canReach = max(canReach, i+nums[i])
        
        if canReach>=len(nums)-1:
            return True
        else:
            return False
            
            
            

        