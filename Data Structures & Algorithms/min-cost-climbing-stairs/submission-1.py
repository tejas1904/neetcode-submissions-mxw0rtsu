import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        
        @functools.lru_cache(maxsize=None)
        def bktrak(i):
            if i==top:
                return 0
            elif i>top:
                return float('inf')
            else:
                one = cost[i]+bktrak(i+1)
                two = cost[i]+bktrak(i+2)

                return min(one,two)
        return min(bktrak(0),bktrak(1))
            