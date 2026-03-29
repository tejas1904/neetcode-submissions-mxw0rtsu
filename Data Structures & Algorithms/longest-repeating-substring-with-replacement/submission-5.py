class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)
        maxfreq = 0
        maxlen = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            freq[char]+=1
            maxfreq = max(maxfreq,freq[char])

            while (r-l+1)-maxfreq > k:
                freq[s[l]]-=1
                maxfreq = max(maxfreq,freq[s[l]])
                l=l+1


            maxlen = max(maxlen,(r-l+1))
        return maxlen




        