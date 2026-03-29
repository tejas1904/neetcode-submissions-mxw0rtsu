import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @functools.lru_cache(None)
        def bktrak(start,csum):
            if csum==amount:
                return 1
            if csum>amount:
                return 0
            else:
                res = []
                for i in range(start,len(coins)):
                    res.append(bktrak(i, csum+coins[i] ))
                
                return sum(res)
        
        return bktrak(start=0 ,csum=0) 
        
        