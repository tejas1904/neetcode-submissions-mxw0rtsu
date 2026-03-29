class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def fn(lsum,rsum,i):
            if i==len(nums) and lsum==rsum:
                return True
            elif i==len(nums) and lsum!=rsum:
                return False
            else:
                elem = nums[i]
                return fn(lsum+elem ,rsum ,i+1) or fn(lsum, rsum+elem ,i+1)
        
        return fn(0,0,0)
        