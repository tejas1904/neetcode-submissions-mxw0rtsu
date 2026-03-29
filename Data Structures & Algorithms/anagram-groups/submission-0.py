class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicta = {}

        for word in strs:
            sword = "".join(sorted(word))
            if sword in dicta:
                dicta[sword].append(word)
            else:
                dicta[sword] = [word]
        
        result = []
        for key in dicta.keys():
            result.append(dicta[key])
        return result
        