from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.g_point_cnt=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.g_point_cnt[tuple(point)] +=1

    def count(self, point: List[int]) -> int:
        x,y = point
        count = 0
        for l in range(1,1000):
            #top-left sq
            p1 = (x,y+l)
            p2 = (x-l,y+l)
            p3 = (x-l,y)
            count=count+(self.g_point_cnt[p1]*self.g_point_cnt[p2]*self.g_point_cnt[p3])


            #top-right sq
            p1 = (x,y+l)
            p2 = (x+l,y+l)
            p3 = (x+l,y)
            count=count+(self.g_point_cnt[p1]*self.g_point_cnt[p2]*self.g_point_cnt[p3])

            #bottom left sq
            p1 = (x-l,y)
            p2 = (x-l,y-l)
            p3 = (x,y-l)
            count=count+(self.g_point_cnt[p1]*self.g_point_cnt[p2]*self.g_point_cnt[p3])

            #bottom rigth sq
            p1 = (x+l,y)
            p2 = (x+l,y-l)
            p3 = (x,y-l)
            count=count+(self.g_point_cnt[p1]*self.g_point_cnt[p2]*self.g_point_cnt[p3])
        return count

           

