class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        self.maxprofit = -float('inf')
        def fn(i,capa,prof):
            
            if i==len(profit):
                if capa<=capacity:
                    self.maxprofit = max(self.maxprofit,prof)
                return
            if capa>capacity:
                return 
            
            
            fn(i+1,capa+weight[i],prof+profit[i])

            fn(i+1,capa,prof)


        fn(0,0,0) 
        return self.maxprofit
