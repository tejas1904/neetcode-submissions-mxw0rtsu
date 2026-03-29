class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastPrice = float('inf')
        maxProfit = 0

        for price in prices:
            leastPrice = min(leastPrice,price)
            profit = price-leastPrice
            maxProfit = max(maxProfit,profit)
        
        return maxProfit
        