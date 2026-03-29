class Solution:
    def rob(self, nums: List[int]) -> int:
        def ROB(nums):
            if len(nums)==2:
                return max(nums[:])
            elif len(nums)>=3:
                cache = [0]*len(nums)
                cache[0] = nums[0]
                cache[1] = max(nums[0],nums[1])

                for i in range(1,len(nums)):
                    cache[i] = max(cache[i-2]+nums[i] , cache[i-1])
                
                return cache[-1]
        
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        else:
            return max(
                ROB(nums[:-1]),
                ROB(nums[1:])
            )

        