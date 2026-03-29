class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            h1 = abs(heapq.heappop(heap))
            h2 = abs(heapq.heappop(heap))

            if h1==h2:
                continue
            else:
                diff = abs(h2-h1)
                heapq.heappush(heap,-diff)
        
        if len(heap)==0:
            return 0
        else:
            return abs(heap[0])
        