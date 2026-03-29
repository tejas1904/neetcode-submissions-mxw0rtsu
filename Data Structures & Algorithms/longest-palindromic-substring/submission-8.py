class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        maxpalin = 1
        palinstring=  s[0]
        for pos in range(len(s)):
            palisize = 1
            i,j = pos-1,pos+1
            while 0<=i and j<len(s):
                if s[i]==s[j]:
                    palisize+=2
                    if palisize>maxpalin:
                        maxpalin = palisize
                        palinstring = s[i:j+1]
                    i=i-1
                    j=j+1
                else:
                    break
        for pos in range(1,len(s)):
            palisize = 0
            i,j = pos-1,pos
            while 0<=i and j<len(s):
                if s[i]==s[j]:
                    palisize+=2
                    if palisize>maxpalin:
                        maxpalin = palisize
                        palinstring = s[i:j+1]
                    i=i-1
                    j=j+1
                else:
                    break


        return palinstring
                