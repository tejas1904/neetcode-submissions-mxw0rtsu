class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in dicta.keys():
                return [dicta[target-num],i]
            else:
                dicta[num] = i

        