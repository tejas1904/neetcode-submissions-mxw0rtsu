class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        memo = {}
        def kp(i,remain_capa):
            if (i,remain_capa) in memo:
                return memo[(i,remain_capa)]
            if i==len(profit):
                return 0
            else:
                include = float('-inf')
                if weight[i]<=remain_capa:
                    include = profit[i] + kp(i+1 , remain_capa-weight[i])
                
                exclude = kp(i+1,remain_capa)

                memo[(i,remain_capa)] = max(include , exclude)
                return memo[(i,remain_capa)]
        
        return kp(0 , capacity)
                    



