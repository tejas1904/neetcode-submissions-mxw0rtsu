class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def backtrack(i,n):
            if n==len(t):
                return 1
            elif i==len(s):
                return 0
            else:
                ways = 0
                for j in range(i,len(s)):
                    if s[j]==t[n]:
                        ways += backtrack(j+1,n+1)
                return ways
                
        
        return backtrack(0,0)
        
            
        