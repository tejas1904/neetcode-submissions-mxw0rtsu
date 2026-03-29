import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @functools.lru_cache(None)
        def bktrak(csum):
            if csum==amount:
                return 0
            if csum>amount:
                return float('inf')
            else:
                res = []
                for coin in coins:
                    res.append(bktrak(csum+coin))
                
                return 1+min(res)
        
        ret = bktrak(csum=0) 
        if ret == float('inf'):
            return -1
        else:
            return ret
        