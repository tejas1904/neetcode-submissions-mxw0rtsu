class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxlen = 0
        seta = set()
        while r<=len(s)-1:
            char = s[r]
            if char in seta:
                seta.remove(s[l])
                l+=1
            else:
                seta.add(char)
                r+=1
            maxlen = max(maxlen,(r-l))
        return maxlen
