class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}

        i=0
        pointer=0
        maxlen = 0
        while i<len(s):
            char = s[i]
            if char in hm and hm[char]>=pointer:
                pointer = hm[char] + 1
                hm[char] = i
            else:
                hm[char] = i
            maxlen = max(maxlen,i-pointer+1)
            i+=1
        return maxlen

