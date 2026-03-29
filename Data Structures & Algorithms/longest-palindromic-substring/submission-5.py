class Solution:
    def longestPalindrome(self, s: str) -> str:

        def lenOfPalindrome(s,l,r):
            while 0<=l and r<=len(s)-1 and s[l]==s[r]:
                l-=1
                r+=1
                
            return s[l+1:r]
        
        maxlen = -100
        maxstr = ""
        for i in range(len(s)):
            strr = lenOfPalindrome(s,l=i,r=i)
            if len(strr)>maxlen:
                maxlen = len(strr)
                maxstr = strr

        for i in range(len(s)-1):
            strr = lenOfPalindrome(s,l=i,r=i+1)
            if len(strr)>maxlen:
                maxlen = len(strr)
                maxstr = strr
        
        return maxstr

        

        