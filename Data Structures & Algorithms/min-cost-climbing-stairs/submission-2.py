import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        mincost = float('inf')
        
        @functools.lru_cache(maxsize=None)
        def bktrak(i,costToHere):
            nonlocal mincost
            if i==top:
                mincost = min(mincost,costToHere)
            elif i>top:
                pass 
            else:
                bktrak(i+1,costToHere+cost[i]),bktrak(i+2,costToHere+cost[i])
                

        one = bktrak(i=0,costToHere=0)
        two = bktrak(i=1,costToHere=0)
        return mincost
            