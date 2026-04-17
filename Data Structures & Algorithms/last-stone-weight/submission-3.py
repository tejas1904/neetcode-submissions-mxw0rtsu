class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for stone in stones:
            heap.append(-stone)
        
        heapq.heapify(heap)
        
        while len(heap)>1:
            s1 = -1*heapq.heappop(heap)
            s2 = -1*heapq.heappop(heap)

            if s1==s2:
                pass
            else:
                nw = abs(s1-s2)
                heapq.heappush(heap,-nw)
        
        return -1*heap[0] if len(heap)==1 else 0