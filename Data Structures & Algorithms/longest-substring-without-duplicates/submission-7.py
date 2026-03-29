class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l=0
        maxlen = 0
        for r in range(len(s)):
            char = s[r]
            if char in hm and hm[char]>=l:
                l = hm[char]+1
            
            hm[char] = r
            
            maxlen = max((r-l)+1,maxlen)
        
        return maxlen
                

