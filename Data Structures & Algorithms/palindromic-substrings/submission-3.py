class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l,r=i,i
            while 0<=l and r<len(s) and s[l]==s[r]:
                count+=1
                l=l-1
                r=r+1
        for i in range(1,len(s)):
            l,r=i-1,i
            while 0<=l and r<len(s) and s[l]==s[r]:
                count+=1
                l=l-1
                r=r+1
        return count

