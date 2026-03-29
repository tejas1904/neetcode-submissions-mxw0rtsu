import functools
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        
        @functools.lru_cache(None)
        def dfs(Lsum,Rsum,i):
            if i==len(nums) and Lsum==Rsum:
                return True
            if  Lsum>sum(nums)/2 or Rsum>sum(nums)/2 or i>len(nums):
                return False
            else:
                return dfs(Lsum+nums[i],Rsum,i+1) or dfs(Lsum,Rsum+nums[i],i+1)
        
        return dfs(0,0,0)
            