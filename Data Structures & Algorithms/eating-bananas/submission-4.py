import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate):
            hours=0
            for pile in piles:
                hours += math.ceil(pile/rate)
            
            return hours<=h
        
        l=1
        r=max(piles)

        bestRate=r
        while l<=r:

            mid = (l+r)//2
            if canEat(rate=mid):
                bestRate=min(bestRate,mid)
                r=mid-1
            elif canEat(rate=mid) == False:
                l=mid+1
            
        return bestRate
        
        




        