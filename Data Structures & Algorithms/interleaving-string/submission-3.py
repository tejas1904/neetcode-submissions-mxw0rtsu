class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def fn(i,j):
            k = i+j

            if (i,j) in memo:
                return memo[(i,j)]
            
            if k==len(s3):
                if i==len(s1) and j==len(s2):
                    return True
                else:
                    return False
            else:
                #by default not possible because the char cannot be taken from either str
                possible = False
                # if char at k matches at s1 take it and explore that branch
                if i<len(s1) and s3[k] == s1[i]:
                    possible = possible or  fn(i+1,j)
                
                # if char at k matches at s2 take it and explore that branch    
                if j<len(s2) and s3[k] == s2[j]:
                    possible = possible or fn(i,j+1)
                memo[(i,j)] = possible
                return memo[(i,j)]
        
        return fn(0,0)



            
            