class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dicta = defaultdict(list)
        heap = []

        for x,y in points:
            dist = math.sqrt((x**2)+(y**2))
            dicta[dist].append([x,y])

            heapq.heappush(heap,dist*-1)
            if len(heap)>k:
                heapq.heappop(heap) 
        
        ans = []
        for dist in heap:
            for point in dicta[dist*-1]:
                ans.append(point)
                if len(ans)>=k:
                    return ans
        
        return ans
        