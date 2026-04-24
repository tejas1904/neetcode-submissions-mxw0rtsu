import functools
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals =sorted(intervals)

        @functools.lru_cache(None)
        def fn(i,j):
            if j==len(intervals):
                return 0
            if intervals[j][0]<intervals[i][1]:
                #its overlapping
                return 1 + min(fn(i,j+1),fn(j,j+1))
            else:
                return 0+fn(j,j+1)
        
        return fn(0,1)
