class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possibleToEat(k_rate):
            my_hours = 0
            for bananas in piles:
                my_hours += math.ceil(bananas/k_rate)
            return my_hours<=h
        
        l=1
        r=max(piles)
        while l<r:
            mid = (l+r)//2
            if possibleToEat(mid):
                r=mid
            else:
                l=mid+1
        return l
        
        