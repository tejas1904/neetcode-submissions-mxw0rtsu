class Solution:
    def canEatPiles(self,rate,pilesa,hours):
        piles = pilesa.copy()
        th = 0
        for pile in piles:
            th += math.ceil(pile/rate)
        if th<=hours:
            return True
        else:
            return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        k = None

        while low<=high:
            rate = (low+high)//2

            if self.canEatPiles(rate,piles,h):
                k = rate
                high = rate-1
            else:
                low = rate + 1
        
        return k
                
