
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def numOfWays(amount):
            if amount in memo:
                return memo[amount]
            if amount<0:
                return float('inf')
            if amount==0:
                return 0
            ways = [float('inf')]*10
            for i in range(len(coins)):
                ways[i] = numOfWays(amount-coins[i])
            
            memo[amount] =  1+min(ways)
            return memo[amount]

        if(numOfWays(amount)) < float('inf'):
            return  numOfWays(amount)
        else:
            return -1
