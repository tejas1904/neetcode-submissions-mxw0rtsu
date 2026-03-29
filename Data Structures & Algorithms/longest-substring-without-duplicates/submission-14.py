class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0

        seta = set()
        maxlen = 0

        while r<len(s):
            while s[r] in seta:
                seta.remove(s[l])
                l+=1
            maxlen = max(maxlen,(r-l+1))
            seta.add(s[r])
            r+=1
        
        return maxlen

        