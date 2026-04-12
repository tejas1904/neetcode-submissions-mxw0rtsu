
import functools
class Solution:
    def checkValidString(self, s: str) -> bool:
        #think of an openig parenthesis as  a '(' as +1 and clsing ')' as a -1 
    
        @functools.lru_cache(None)
        def dp(i,delta):
            if delta<0:
                return False
            
            if i==len(s):
                if delta==0:
                    return True
                else:
                    return False
            
            char = s[i]
            if char=='(':
                return dp(i+1,delta+1)
            elif char==')':
                return dp(i+1,delta-1)
            else:
                return dp(i+1,delta+1) or dp(i+1,delta-1) or dp(i+1,delta)
        
        return dp(0,0)
            
            
            
        