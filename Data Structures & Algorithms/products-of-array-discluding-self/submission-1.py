class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accumulator1 = [1]*len(nums)
        for i in range(1,len(nums)):
            accumulator1[i] = accumulator1[i-1]*nums[i-1]
        
        accumulator2 = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            accumulator2[i] = accumulator2[i+1]*nums[i+1]
        
        for i in range(len(accumulator1)):
            accumulator1[i]*=accumulator2[i]
        
        return accumulator1

        