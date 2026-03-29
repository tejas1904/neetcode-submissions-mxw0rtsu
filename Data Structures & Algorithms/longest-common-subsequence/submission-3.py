class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp  = [[0]*(len(text1)+1) for _ in range(len(text2))]
        #filling row 0
        i=0
        for j in range(1,len(text1)+1):
            if text2[0]==text1[j-1]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] 
        
        for i in range(1,len(text2)):
            for j in range(1,len(text1)+1):

                if text2[i]==text1[j-1]:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1] ,1+dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return dp[-1][-1]