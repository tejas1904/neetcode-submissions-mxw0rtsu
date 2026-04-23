class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals , key= lambda x: (x[0],x[0]))

        ans  = [intervals[0]]
        for s,e in intervals[1:]:
            if s<=ans[-1][1]:
                ans[-1][0] = min(ans[-1][0],s)
                ans[-1][1] = max(ans[-1][1],e)
            else:
                ans.append([s,e])
        return ans
