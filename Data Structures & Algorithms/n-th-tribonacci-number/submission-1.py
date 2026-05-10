class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def tribo(n):
            if n in memo:
                return memo[n]
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            
            memo[n]=tribo(n-1)+tribo(n-2)+tribo(n-3)
            return memo[n]
        
        return tribo(n)
        