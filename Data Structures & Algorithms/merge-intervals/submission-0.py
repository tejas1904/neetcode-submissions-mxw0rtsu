class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals,key = lambda x:(x[0],x[1]))

        ans = [intervals[0]]

        
        for s,e in intervals[1:]:
            ans_end = ans[-1][1]
            if s<=ans_end:
                ans[-1][1] = max(e,ans[-1][1])
            else:
                ans.append([s,e])
        
        return ans

