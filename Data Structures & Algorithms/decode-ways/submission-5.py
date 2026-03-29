import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @functools.lru_cache(None)
        def backtrack(i,j):
            if s[i]=='0':
                return 0
            elif j>=len(s):
                return 0
            elif int(s[i:j+1])>26:
                return 0
            elif j==len(s)-1:
                return 1
            else:
                return backtrack(j+1,j+1) + backtrack(j+1,j+2)
        
        return backtrack(i=0,j=0) + backtrack(i=0,j=1)
            


        