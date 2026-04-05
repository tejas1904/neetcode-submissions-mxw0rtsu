class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSeen = nums[0]
        sumTillHere = nums[0]

        for i in range(1,len(nums)):
            if nums[i]+sumTillHere>=nums[i]:
                sumTillHere += nums[i]
            else:
                sumTillHere = nums[i]
            maxSeen = max(maxSeen,sumTillHere)
        return maxSeen


            