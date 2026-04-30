from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = defaultdict(list)
        for s,d,t in times:
            adjList[s].append([d,t])

        distances = [float('inf')]*(n+1)
        visited  = set()

        heap = [(0,k)]

        while heap:
            currDist,node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            distances[node] = currDist
            
            for nbr,dst in adjList[node]:
                newDist = dst+currDist
                if newDist<distances[nbr]:
                    heapq.heappush(heap,(newDist,nbr))
        
        max_dist = max(distances[1:])
        return max_dist if max_dist != float('inf') else -1
            







