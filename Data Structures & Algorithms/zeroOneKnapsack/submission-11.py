class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        dp = [[0]*(capacity+1) for _ in range(len(profit)+1)]

        for i in range(1,len(profit)+1):
            for bag_capacity in range(1,capacity+1):
                if weight[i-1]<=bag_capacity:
                    dp[i][bag_capacity] = max(
                        dp[i-1][bag_capacity],
                        dp[i-1][bag_capacity - weight[i-1]] + profit[i-1]
                    )
                else:
                    dp[i][bag_capacity] = dp[i-1][bag_capacity]
        
        return dp[len(profit)][capacity]
