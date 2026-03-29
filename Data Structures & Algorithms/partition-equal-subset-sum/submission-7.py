class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        target = sum(nums)//2

        memo = {}
        def fn(tsum,i):
            if (tsum,i) in memo:
                return memo[(tsum,i)]
            if i==len(nums) and tsum==target:
                return True
            elif i==len(nums) and tsum!=target:
                return False
            else:
                elem = nums[i]
                memo[(tsum,i)] =  fn(tsum+elem , i+1) or fn(tsum ,i+1)
                return memo[(tsum,i)]
        return fn(0,0)
        