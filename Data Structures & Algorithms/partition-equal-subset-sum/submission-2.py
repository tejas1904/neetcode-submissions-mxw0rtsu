class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def fn(i,s1,s2):
            if i==len(nums):
                if s1==s2:
                    return True
                else:
                    return False
            
            if fn(i+1, s1+nums[i] ,s2):
                return True
            if fn(i+1, s1 , s2+nums[i]):
                return True
            
            return False
        
        return fn(0,0,0)