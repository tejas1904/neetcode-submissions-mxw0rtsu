class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        dp = [[0]*(capacity+1) for _ in range(len(profit)+1)] 
        
        for i in range(1,len(profit)+1):
            for bag_capa in range(1,capacity+1):
                not_include = dp[i-1][bag_capa]

                include = 0
                if weight[i-1]<=bag_capa:
                    include = dp[i-1][bag_capa-weight[i-1]]+profit[i-1]
                
                dp[i][bag_capa] = max(include,not_include)
        
        return dp[-1][-1]



