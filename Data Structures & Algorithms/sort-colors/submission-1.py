class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0,0,0]

        for num in nums:
            buckets[num] += 1
        
        i = 0
        for n in range(len(buckets)):
            for j in range(buckets[n]):
                nums[i] = n
                i += 1

        