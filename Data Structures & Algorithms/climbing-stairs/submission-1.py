class Solution:
    hm  = {}
    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        if n==0:
            return 1
        if n in self.hm.keys():
            return self.hm[n]
        
        else:
            self.hm[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.hm[n]