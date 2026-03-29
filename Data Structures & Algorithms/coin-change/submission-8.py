class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)

        for wallet_capacity in range(1,amount+1):
            poss = [float('inf')]
            for coin in coins:
                if wallet_capacity-coin>=0:
                    poss.append(1+dp[wallet_capacity-coin])
                dp[wallet_capacity] = min(poss) 
        
        return -1 if dp[-1]==float('inf') else dp[-1] 
        