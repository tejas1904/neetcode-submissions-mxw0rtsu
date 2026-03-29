class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dicta = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target-num
            if diff in dicta:
                return [dicta[diff],i]
            else:
                dicta[num] = i
        