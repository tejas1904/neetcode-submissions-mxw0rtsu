class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(validWindowDict,windowDict):
            for key in validWindowDict:
                if windowDict[key]>=validWindowDict[key]:
                    pass
                else:
                    return False
            return True
        
        if(len(t)>len(s)):
            return ""
        validWindowDict = {}
        windowDict = defaultdict(int)
        for char in t:
            validWindowDict[char] = validWindowDict.get(char,0)+1
            windowDict[char] = 0

        minlen = float('inf')
        start = 0
        i=0
        for j in range(len(s)):

            windowDict[s[j]] = windowDict[s[j]]+1;
                
            while valid(validWindowDict,windowDict):
                if (j-i+1)<minlen:
                    start = i
                    minlen = (j-i+1)

                windowDict[s[i]] = windowDict[s[i]] - 1;
                i+=1;
        if minlen!=float('inf'):
            return s[start:start+minlen]
        else:
            return ""

        