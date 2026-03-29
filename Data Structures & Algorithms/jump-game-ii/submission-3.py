from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def jg(pos: int) -> int:
            if pos == n - 1:
                return 0
            if pos >= n:
                return float('inf')

            best = float('inf')
            for step in range(1, nums[pos] + 1):
                best = min(best, jg(pos + step))
            return 1 + best

        return jg(0)

        