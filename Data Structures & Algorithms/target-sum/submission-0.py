class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def fn(i,t):
            if i==len(nums):
                if t==target:
                    return 1
                else:
                    return 0
            if i>len(nums):
                return 0
            
            return (
                fn(i+1 , t+nums[i])
                +
                fn(i+1 , t-nums[i])
            )
        return fn(0,0)

        