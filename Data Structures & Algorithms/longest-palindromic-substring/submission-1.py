class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstr=""
        
        for center in range(len(s)):
            i=center
            j=center

            while i>=0 and j<=len(s)-1:
                if s[i]==s[j]:
                    leng = j-i+1
                    if leng>len(maxstr):
                        maxstr = s[i:j+1]
                else:
                    break
                i = i-1
                j = j+1

            
            i=center
            j=center+1

            while i>=0 and j<=len(s)-1:
                if s[i]==s[j]:
                    leng = j-i+1
                    if leng>len(maxstr):
                        maxstr = s[i:j+1]
                else:
                    break
                i = i-1
                j = j+1
        
        return maxstr
                


        