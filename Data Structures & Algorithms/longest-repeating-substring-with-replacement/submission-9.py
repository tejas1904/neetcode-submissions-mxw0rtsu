class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j = 0,0
        freq= {}
        maxFreqElem = s[0]
        maxlen = 0
        
        for char in s:
            freq[char] = 0
        
        while j<len(s):
            char = s[j]
            freq[char]+=1
            if freq[char]>freq[maxFreqElem]:
                maxFreqElem = char
            maxFreq = freq[maxFreqElem]
            while (j-i+1)-maxFreq > k:
                freq[s[i]]-=1
                i+=1
                

            maxlen = max(maxlen,(j-i+1))
            j+=1
        return maxlen
            



        