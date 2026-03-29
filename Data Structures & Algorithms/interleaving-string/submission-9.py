class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        n = len(s1)
        m = len(s2)
        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True
        # First column (only s1)
        for i in range(1, n+1):
            k=i-1
            if s1[i-1] == s3[k]:
                dp[i][0] = dp[i-1][0]

        # First row (only s2)
        for j in range(1, m+1):
            k = j-1
            if s2[j-1] == s3[k]:
                dp[0][j] = dp[0][j-1]

        for i in range(1,n+1):
            for j in range(1,m+1):
                k=i+j-1
                
                if s1[i-1]==s3[k]:
                    dp[i][j] = dp[i-1][j]
                elif s2[j-1]==s3[k]:
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]
        