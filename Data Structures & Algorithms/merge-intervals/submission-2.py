class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:(x[0],x[1]))
        
        
        ans = [intervals[0]]
        for s,e in intervals:
            lastS,lastE = ans[-1]
            if s<=lastE:
                ans[-1][1] = max(ans[-1][1] , e)
            else:
                ans.append([s,e])
        
        return ans
