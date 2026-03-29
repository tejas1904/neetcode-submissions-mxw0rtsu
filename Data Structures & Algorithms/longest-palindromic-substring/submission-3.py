class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        maxstr = ""
        for p in range(0,n+1):##going over all diagonals of matrix
            i=0
            j=i+p

            while j<=n-1: 
                if s[i]==s[j]:
                    if (i==j) or ((j-i)+1 == 2): #string of length 1 or 2
                        dp[i][j] = True
                        substr = s[i:j+1]
                        if len(substr)>len(maxstr):
                            maxstr = substr
                    elif dp[i+1][j-1] == 1: #if bottom left also a palindrome
                        dp[i][j] = True
                        substr = s[i:j+1]
                        if len(substr)>len(maxstr):
                            maxstr = substr

                i+=1
                j=i+p
        
        return maxstr
        