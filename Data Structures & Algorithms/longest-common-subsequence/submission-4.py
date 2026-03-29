from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def fn(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            else:
                if text1[i]==text2[j]:
                    return 1 + fn(i+1,j+1)
                else:
                    return max(fn(i+1,j) , fn(i,j+1))
        
        return fn(0,0)