class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicta = {}
        

        for string in strs:
            freqlist = [0]*26
            for char in string:
                freqlist[ord(char)-ord('a')]+=1
            freqlist = tuple(freqlist)

            if freqlist in dicta:
                dicta[freqlist].append(string)
            else:
                dicta[freqlist] = [string]
        
        result = []
        for key in dicta:
            result.append(dicta[key])
        return result