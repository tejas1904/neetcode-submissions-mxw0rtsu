class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            length = len(word)
            s = s + f"{length}#{word}"
        return s
    
    def decode(self, s: str) -> List[str]:
        i=0
        array = []
        while i< len(s):
            wordlen = ""
            while s[i]!='#':
                wordlen += s[i]
                i=i+1
            i=i+1
            wordlen = int(wordlen)
            substring = s[i : (i+wordlen)]
            array.append(substring)
            i = i + wordlen
        
        return array

