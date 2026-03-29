class Solution:
    def climbStairs(self, n: int) -> int:
        
        hm = {} 
        def climber(i):
            if i in hm:
                return hm[i]
            if i>n:
                return 0
            if i==n:
                return 1
            
            Bone =  climber(i+1)
            Btwo = climber(i+2)

            hm[i]= Bone+Btwo
            
            return Bone+Btwo
        
        return climber(0)
        
        
            
        