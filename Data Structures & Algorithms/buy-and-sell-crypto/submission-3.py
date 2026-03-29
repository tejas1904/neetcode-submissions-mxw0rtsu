class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxNoToRight=0
        maxprofit = 0
        for i in range(len(prices)-1,-1,-1):
            possibleProfit =max(maxNoToRight,prices[i]) - prices[i]
            maxprofit = max(maxprofit,possibleProfit)

            maxNoToRight = max(prices[i],maxNoToRight)
        
        return maxprofit

        