class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarraySum = 0
        maxseen = -float('inf')
        for num in nums:
            maxSubarraySum = max(num, maxSubarraySum+num)
            maxseen = max(maxseen ,maxSubarraySum )
        
        return maxseen

        