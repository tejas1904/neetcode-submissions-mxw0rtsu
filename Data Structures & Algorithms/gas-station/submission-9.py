from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        level = 0
        i, j = 0, 0

        while j < len(nums) - 1:
            farthest = j
            for k in range(i, j + 1):
                farthest = max(farthest, k + nums[k])

            i = j + 1
            j = farthest
            level += 1

        return level