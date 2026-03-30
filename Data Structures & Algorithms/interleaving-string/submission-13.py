import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False

        @functools.lru_cache(None)
        def fn(i,j):
            k=i+j
            if k==len(s3):
                return True
            ret1,ret2 = False,False
            if i<len(s1) and s3[k]==s1[i]:
                ret1 = fn(i+1,j)
            if j<len(s2) and s3[k]==s2[j]:
                ret2 = fn(i,j+1)
            return ret1 or ret2
        
        return fn(0,0)


        