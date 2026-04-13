from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        future = {}

        for char in s:
            future[char] = future.get(char, 0) + 1

        ans = []
        keys = set()
        start = 0

        for i in range(len(s)):
            keys.add(s[i])
            future[s[i]] -= 1

            allZeros = True
            for key in keys:
                if future[key] > 0:
                    allZeros = False

            if allZeros:
                ans.append(i - start + 1)
                start = i + 1
                keys = set()

        return ans