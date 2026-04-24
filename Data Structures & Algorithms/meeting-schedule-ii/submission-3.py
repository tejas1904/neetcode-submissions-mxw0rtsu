"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        intervals = sorted([[x.start, x.end] for x in intervals])


        #meetingRoom[i] is the end time of that room
        meetingRooms = [0]

        for s,e in intervals:
            if meetingRooms[0]<=s:
                meetingRooms[0]=e
                heapq.heapify(meetingRooms)
            else:
                heapq.heappush(meetingRooms,e)
        
        return len(meetingRooms)
        