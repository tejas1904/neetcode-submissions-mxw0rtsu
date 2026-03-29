
from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def fn(i,j):
            if i==len(word1) and j==len(word2):
                return 0
            elif i==len(word1):
                return len(word2)-j
            elif j==len(word2):
                return len(word1)-i
            else:

                if word1[i]==word2[j]:
                    return fn(i+1,j+1)
                else:
                    return min(
                        1 +fn(i+1,j+1), #replace
                        1+ fn(i+1,j),#delete from w1
                        1+ fn(i,j+1)#insert char at w1
                    )
        return fn(0,0)