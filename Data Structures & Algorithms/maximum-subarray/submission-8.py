class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        maxTillHere = [0]*len(nums)
        maxTillHere[0] = nums[0]
    
        
        for i in range(1,len(nums)):
            if nums[i]+maxTillHere[i-1] > nums[i]:
                maxTillHere[i] = nums[i]+maxTillHere[i-1]
            else:
                maxTillHere[i] = nums[i]
        
        return max(maxTillHere)
