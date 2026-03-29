class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def fn(total,i):
            if (total,i) in memo:
                return memo[(total,i)]
            if i==len(nums) and total==target:
                return 1
            elif i==len(nums) and total!=target:
                return 0
            
            memo[(total,i)]=  fn(total+nums[i] , i+1)  + fn(total-nums[i] , i+1)
            return memo[(total,i)]
            
        return fn(0,0)
