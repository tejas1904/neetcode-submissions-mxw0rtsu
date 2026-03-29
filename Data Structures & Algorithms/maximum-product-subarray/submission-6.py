class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = [0]*len(nums)
        minProd = [0]*len(nums)

        maxProd[0] , minProd[0] = nums[0],nums[0]

        for i in range(1,len(nums)):
            num = nums[i]
            maxp =  maxProd[i-1]*num
            minp = minProd[i-1]*num
            maxProd[i] = max(
                num,
                maxp,
                minp
            )

            minProd[i] = min(
                num,
                maxp,
                minp
            )
        
        return max(maxProd+minProd)