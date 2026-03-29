class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def buy(i):
            if i>=len(prices)-1:
                return 0
            elif i ==len(prices)-2:
                return prices[i+1]-prices[i]
            else:
                acc = [buy(i+1)]
                for j in range(i+1,len(prices)):
                    acc.append((prices[j]-prices[i])+buy(j+2))
                return max(acc)
            
        ret = buy(0) 
        if ret>0:
            return ret
        else:
            return 0
            