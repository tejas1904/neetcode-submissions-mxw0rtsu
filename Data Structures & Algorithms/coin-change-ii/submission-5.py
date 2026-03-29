class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)

        dp = [[0]*(amount+1) for _ in range(len(coins))]

        #first col is 1
        for i in range(len(coins)):
            dp[i][0] = 1

        coin = coins[0]
        for amt in range(0,amount+1):
            if coin<=amt:
                dp[0][amt] = 1 if dp[0][amt-coin] == 1 else 0
        
        for i in range(1,len(coins)):
            for amt in range(1,amount+1):
                #number of ways not using the coin
                dp[i][amt] = dp[i][amt] + dp[i-1][amt]
                #number ways usign the coin
                coin = coins[i]
                if dp[i][amt-coin] >= 1:
                    dp[i][amt] = dp[i][amt] + dp[i][amt-coin]
        
        return dp[-1][-1]
                



