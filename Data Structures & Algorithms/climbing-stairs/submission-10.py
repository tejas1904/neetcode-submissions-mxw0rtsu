class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def bktrak(i):
            if i in memo:
                return memo[i]
            elif i==n:
                return 1
            elif i>n:
                return 0
            else:
                memo[i] =  bktrak(i+1) + bktrak(i+2)
                return memo[i]
        
        return bktrak(0)