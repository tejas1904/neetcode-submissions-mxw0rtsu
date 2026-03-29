class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstr = ""
        for center in range(len(s)):
            i=center
            j=center
            
            while 0<=i and j<=len(s)-1:
                if s[i]==s[j]:
                    
                    substr = s[i:j+1]
                    if len(substr)>=len(maxstr):
                        maxstr  = substr
                    i = i-1
                    j = j+1
                else:
                    break
            
            i=center
            j=center+1
            
            while 0<=i and j<=len(s)-1:
                if s[i]==s[j]:
                    
                    substr = s[i:j+1]
                    if len(substr)>=len(maxstr):
                        maxstr  = substr
                    i = i-1
                    j = j+1
                else:
                    break
        
        return maxstr


        