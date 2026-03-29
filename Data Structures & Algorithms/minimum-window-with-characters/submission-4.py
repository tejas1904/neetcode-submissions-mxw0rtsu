from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(validWindowDict, windowDict):
            for key in validWindowDict:
                if windowDict[key] < validWindowDict[key]:
                    return False
            return True

        if len(t) > len(s):
            return ""

        validWindowDict = {}
        windowDict = defaultdict(int)

        for char in t:
            validWindowDict[char] = validWindowDict.get(char, 0) + 1

        minlen = float('inf')
        start_index = 0
        i = 0

        for j in range(len(s)):
            windowDict[s[j]] += 1

            while valid(validWindowDict, windowDict):
                # update best window
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                    start_index = i

                # shrink window
                windowDict[s[i]] -= 1
                i += 1

        return "" if minlen == float('inf') else s[start_index:start_index + minlen]
