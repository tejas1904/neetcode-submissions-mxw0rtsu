class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        targetSum = sum(nums)//2

        memo = {}

        def fn(i,cs):
            if (i,cs) in memo:
                return memo[(i,cs)]
            if i>len(nums):
                return False
            if i==len(nums):
                if cs==targetSum:
                    return True
                else:
                    return False
            
            memo[(i,cs)] = (
                fn(i+1, cs)
                or
                fn(i+1, cs+nums[i])
            )
            return memo[(i,cs)]
            
        return fn(0,0)
        