class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(currsum):
            if currsum in memo:
                return memo[currsum]
            if currsum==amount:
                return 0
            if currsum>amount:
                return float('inf')
            minlen = float('inf')
            for coin in coins:
                lenn = dfs(currsum+coin)
                minlen = min(minlen,lenn)
            memo[currsum] = 1+minlen
            return memo[currsum]
        
        ans = dfs(0)
        if ans!=float('inf'):
            return ans
        else:
            return -1

