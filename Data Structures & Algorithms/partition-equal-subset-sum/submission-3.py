class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        targetSum = sum(nums)//2

        def fn(i,cs):
            if i>len(nums):
                return False
            if i==len(nums):
                if cs==targetSum:
                    return True
                else:
                    return False
            
            return (
                fn(i+1, cs)
                or
                fn(i+1, cs+nums[i])
            )
            
        return fn(0,0)
        