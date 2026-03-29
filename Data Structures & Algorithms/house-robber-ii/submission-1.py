class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def ROB(start,end):
            if (start,end) in memo:
                return memo[(start,end)]
            if start>end:
                return 0
            elif start==end:
                return nums[start]
            else:
                memo[(start,end)] =  max(
                    nums[start]+ROB(start+2,end),
                    ROB(start+1,end)
                )
                return memo[(start,end)]
        start = 0
        end = len(nums)-1
        return max(
                    nums[start]+ROB(start+2,end-1),
                    ROB(start+1,end)
                )