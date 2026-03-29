import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @functools.lru_cache(None)
        def fn(i,j,k):
            
            if i==len(s1) and j==len(s2) and k==len(s3):
                return True
            
            
            ret1,ret2 = False,False
            if i<len(s1) and k<len(s3) and s1[i]==s3[k]:
                ret1 = fn(i+1,j,k+1)
            
            if j<len(s2) and k<len(s3) and s2[j]==s3[k]:
                ret2 = fn(i,j+1,k+1)
            
            return ret1 or ret2
        
        return fn(0,0,0)

           
            
