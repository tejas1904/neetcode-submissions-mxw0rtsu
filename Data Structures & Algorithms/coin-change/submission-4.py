class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]

        dp[0]=0
        for i in range(1,amount+1):
            prevs = [float('inf')]
            for coin in coins:
                if i-coin>=0:
                    prevs.append(dp[i-coin])
            
            dp[i] = 1 + min(prevs)
        
        if dp[-1]==float('inf'):
            return -1
        else:
            return dp[-1]
        