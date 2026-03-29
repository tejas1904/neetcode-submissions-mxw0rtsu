class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seta = set()
        longest = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in seta:
                seta.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                seta.remove(s[l])
                l += 1

        return longest
