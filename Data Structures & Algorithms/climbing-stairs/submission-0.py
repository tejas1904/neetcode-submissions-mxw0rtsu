class Solution:
    def climbStairs(self, n: int) -> int:
        dicta ={}
        def climb(n):
            if n==0:
                return 1
            elif n<0:
                return 0
            else:
                try:
                    return dicta[n]
                except:
                    dicta[n] =  climb(n-1)+climb(n-2)
                    return dicta[n]
        return climb(n)
        