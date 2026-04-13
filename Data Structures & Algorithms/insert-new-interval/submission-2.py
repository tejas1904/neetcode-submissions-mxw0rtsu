class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        inserted = False
        for i in range(len(intervals)-1):
            s,e = newInterval
            s1,e1 = intervals[i]
            s2,e2 = intervals[i+1]

            if s1<=s and s<=s2:
                intervals.insert(i+1,newInterval)
                inserted=True
                break
        if not inserted:
            s,e = newInterval
            s1,e1 = intervals[0]
            if s<s1:
                intervals.insert(0,newInterval)
            else:
                intervals.append(newInterval)

        ans = [intervals[0]]
        for s,e in intervals[1:]:
            ls,le = ans[-1]
            if le>=s:
                ans[-1][1] = max(ans[-1][1] , e)
            else:
                ans.append([s,e])
        
        return ans
        