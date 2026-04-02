import functools
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        paslens = [1, 7, 30]

        @functools.lru_cache(None)
        def dp(start):
            if start >= len(days):
                return 0

            mincosts = []
            for i in range(3):
                passlen = paslens[i]
                cost = costs[i]

                j = start
                while j < len(days) and days[j] < days[start] + passlen:
                    j += 1

                mincosts.append(cost + dp(j))

            return min(mincosts)

        return dp(0)