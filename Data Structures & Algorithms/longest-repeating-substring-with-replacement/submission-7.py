class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def getmaxfreq(dicta):
            maxfreq = 0
            for key in dicta.keys():
                maxfreq = max(maxfreq,dicta[key])
            return maxfreq
        
        freq = defaultdict(int)
        maxlen = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            freq[char]+=1

            while (r-l+1)-getmaxfreq(freq) > k:
                freq[s[l]]-=1
                l=l+1


            maxlen = max(maxlen,(r-l+1))
        return maxlen




        