from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList=  defaultdict(list)
        for i,j,d in times:
            adjList[i].append((j,d))

        visited = set()
        times = [-1]*(n+1)
        
        heap = [(0,k)]

        while heap:
            dist,node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            times[node]=dist

            for nbr,dist2 in adjList[node]:
                if nbr not in visited:
                    heapq.heappush(heap,(dist+dist2,nbr))  
        
        if -1 in times[1:]:
            return -1
        else:
            return max(times[1:])
              
           
