class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtrack(total):
            if total==amount:
                return 0
            if total>amount:
                return float('inf')
            if total in memo:
                return memo[total]
            
            res = []
            for coin in coins:
                res.append(backtrack(total+coin))
            
            memo[total] = 1+min(res)
            return memo[total]
        
        ret = backtrack(0)
        if ret==float('inf'):
            return -1
        else:
            return ret
