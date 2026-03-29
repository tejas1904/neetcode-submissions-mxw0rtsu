class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        lcs = [[0 for i in range(l1+1)] for i in range(l2+1)]

        for i in range(1,l2+1):
            for j in range(1,l1+1):
                if (text2[i-1]!=text1[j-1]):
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
                else:
                    lcs[i][j] = lcs[i-1][j-1] + 1
        
        return lcs[l2][l1]
        