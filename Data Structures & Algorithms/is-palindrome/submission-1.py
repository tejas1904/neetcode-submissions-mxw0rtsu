class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = s.lower()
        stra = ""
        for char in s:
            if (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9')):
                stra = stra+char
        
        s = stra

        l = 0
        h  =len(s)-1

        while l<h:
            if s[l]!=s[h]:
                return False
            l+=1
            h-=1

    
        return True
            
        