from collections import defaultdict
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dicta = {}
        for num in queries:
            dicta[num] = float('inf')
        
        for s,e in intervals:
            intervalLen = (e-s)+1
            for ts in range(s,e+1):
                if ts in dicta.keys():
                    dicta[ts] = min(dicta[ts],intervalLen)
        
        ans = []
        for num in queries:
            minLen = dicta[num]
            ans.append(minLen if minLen!=float('inf') else -1)
        return ans

        