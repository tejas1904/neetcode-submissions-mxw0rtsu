class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod=[0]*len(nums) #most positive product
        minprod=[0]*len(nums) #most negative product
        
        maxprod[0] = nums[0]
        minprod[0] = nums[0]

        for i in range(1,len(nums)):
            maxprod[i] = max(
                nums[i]*maxprod[i-1],
                nums[i]*minprod[i-1],
                nums[i]
            )

            minprod[i] = min(
                nums[i]*maxprod[i-1],
                nums[i]*minprod[i-1],
                nums[i]
            )
        
        return max(maxprod)