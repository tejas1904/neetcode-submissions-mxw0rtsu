class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)-1
        dp = [[0]*(capacity+1) for _ in range(n+1)]

        #fill out row 0
        for bag_capa in range(1,capacity+1):
            if weight[0]<=bag_capa:
                dp[0][bag_capa] = profit[0]
        
        for i in range(1,n+1):
            for bag_capa in range(1,capacity+1):
                
                exclude = dp[i-1][bag_capa]
                include = 0    
                if weight[i] <= bag_capa:
                    include = dp[i-1][bag_capa - weight[i]] + profit[i]
                
                dp[i][bag_capa] = max(include , exclude)
        
        return dp[-1][-1]
                  

