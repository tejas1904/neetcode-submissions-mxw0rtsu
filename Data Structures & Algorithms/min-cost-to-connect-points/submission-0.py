import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(point) for point in points]

        def dist(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        heap = [(0,points[0])]
        visited = set()

        
        distSum = 0
        while len(visited) < len(points):
            d,np = heapq.heappop(heap)

            if np in visited:
                continue

            visited.add(np)
            distSum += d

            for p2 in points:
                if p2 not in visited:
                    heapq.heappush(heap, (dist(np, p2), p2))

        return distSum