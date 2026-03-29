class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceSeenTillNow = prices[0]
        maxProfit = 0
        for price in prices:
            profit = price-minPriceSeenTillNow
            maxProfit = max(maxProfit , profit)
            minPriceSeenTillNow = min(minPriceSeenTillNow,price)
        
        return maxProfit


        