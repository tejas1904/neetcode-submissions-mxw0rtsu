class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def backtrack(i,strr):
            if len(strr)==len(t) and strr==t:
                return 1
            elif i==len(s):
                return 0
            else:
                ways = 0
                for j in range(i,len(s)):
                    ways += backtrack(j+1,strr+s[j])
                return ways
        
        return backtrack(0,"")
        
            
        