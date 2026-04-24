"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals,key = lambda x : (x.start,x.end))
        for i in range(1,len(intervals)):
            prev = i-1
            this = i
            if intervals[this].start<intervals[prev].end:
                return False
        return True
