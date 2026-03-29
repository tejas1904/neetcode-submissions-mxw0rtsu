class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def kp(i,remain_capa,curr_prof):
            if i==len(profit):
                return curr_prof
            else:
                include = float('-inf')
                if weight[i]<=remain_capa:
                    include = kp(i+1 , remain_capa-weight[i] , curr_prof+profit[i])
                
                exclude = kp(i+1,remain_capa,curr_prof)

                return max(include , exclude)
        
        return kp(0 , capacity , 0)
                    



