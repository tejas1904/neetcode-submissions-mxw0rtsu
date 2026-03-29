class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numdict={}
        for i in range(len(nums)):
            num=nums[i]
            diff = target-num
            if diff in numdict:
                return [numdict[diff],i]
            else:
                numdict[num]=i

        