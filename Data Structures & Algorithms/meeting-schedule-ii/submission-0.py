class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        rooms = [0] * len(intervals)

        intervals = sorted([[x.start, x.end] for x in intervals])

        for s, e in intervals:
            for i in range(len(rooms)):
                if s >= rooms[i]:
                    rooms[i] = e
                    break

        return sum(1 for x in rooms if x > 0)