import functools
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        @functools.lru_cache(None)
        def fn(i,lsum,rsum):
            if i==len(stones):
                return abs(lsum-rsum)
            else:
                return min(
                    fn(i+1,lsum+stones[i],rsum),
                    fn(i+1,lsum,rsum+stones[i])
                )
        return fn(0,0,0)