class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins))]

        #fill 0th colums
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for j in range(1,amount+1):
            if j%coins[0]==0:
                dp[0][j] = 1
        
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                dp[i][j] +=  dp[i-1][j]
                if coins[i]<=j:
                    dp[i][j] +=  dp[i][j-coins[i]]
                
        return dp[-1][-1]

        