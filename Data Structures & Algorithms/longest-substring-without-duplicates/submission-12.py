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
                maxlen = max(maxlen,(r-l)+1)
                r+=1
        return maxlen
