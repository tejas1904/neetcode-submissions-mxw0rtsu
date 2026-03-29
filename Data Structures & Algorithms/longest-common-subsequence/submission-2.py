class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def fn(i,j):
            if (i,j) in memo:
                return memo[(i,j)] 
            if i==len(text1) or j==len(text2):
                return 0
            else:
                if text1[i]==text2[j]:
                    memo[(i,j)] =  1 + fn(i+1,j+1)
                else:
                    memo[(i,j)] = max(fn(i+1,j) , fn(i,j+1))
                return memo[(i,j)]

        return fn(0,0) 
