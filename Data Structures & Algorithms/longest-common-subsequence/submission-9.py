import functools
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @functools.lru_cache(None)
        def bktrak(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            else:
                if text1[i]==text2[j]:
                    return 1+bktrak(i+1,j+1)
                else:
                    return max(bktrak(i+1,j),bktrak(i,j+1))
        
        return bktrak(0,0)

        