import functools
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        @functools.lru_cache(None)
        def fn(i,mcount,ncount):
            if i==len(strs):
                return 0
            else:
                ret1 = fn(i+1,mcount,ncount)
                
                oc,zc = 0,0
                for char in strs[i]:
                    if char=='0':
                        zc+=1
                    elif char=='1':
                        oc+=1
                ret2 = -float('inf')
                if mcount+zc <= m and ncount+oc<= n:
                    ret2 = 1 + fn(i+1,mcount+zc,ncount+oc)
                
                return max(ret1,ret2)
        
        return fn(0,0,0)
