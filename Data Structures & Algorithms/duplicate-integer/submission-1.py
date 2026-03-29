class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countSet = set()
        for num in nums:
            if num in countSet:
                return True
            else:
                countSet.add(num);
        return False