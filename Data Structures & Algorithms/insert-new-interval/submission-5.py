class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        inserted = False

        if len(intervals)==0:
            intervals.append(newInterval)
        
        #insert in the begining
        if not inserted and newInterval[1]<intervals[0][0]:
            ans.append(newInterval)
            inserted = True
        #try inserign the new Interval in between
        for s,e in intervals:
            if (not inserted) and (newInterval[0]<=s):
                ans.append(newInterval)
                inserted = True
            
            ans.append([s,e])
        #try insert at the end
        if not inserted:
            ans.append(newInterval)
            inserted = True
        
        ans2 = [ans[0]]
        for s,e in ans[1:]:
            if s<=ans2[-1][1]:
                ans2[-1][0] = min(ans2[-1][0],s)
                ans2[-1][1] = max(ans2[-1][1],e)
            else:
                ans2.append([s,e])

        return ans2     