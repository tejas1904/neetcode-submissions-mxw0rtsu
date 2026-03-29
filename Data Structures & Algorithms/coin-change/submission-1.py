class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(total=0):
            if total==amount:
                return 0
            if total>amount:
                return float('inf')
            if total in memo:
                return memo[total]
            
            ret = []
            for coin in coins:
                ret.append(dfs(total+coin))
            
            memo[total] = 1+min(ret)
            return memo[total]
        
        ret = dfs(0)
        if ret==float('inf'):
            return -1
        else:
            return ret
    
        
                    
