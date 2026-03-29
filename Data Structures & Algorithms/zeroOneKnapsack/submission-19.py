class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def bktrak(i,capa,prof):
            if i==len(profit):
                return prof
            else:
                
                    
                    not_include = bktrak(i+1,capa,prof)

                    include = 0
                    if weight[i]+capa <= capacity:
                        include = bktrak(i+1, capa+weight[i], prof+profit[i])
                    
                    return max(not_include , include)
        
        return bktrak(i=0, capa=0, prof=0)
                
