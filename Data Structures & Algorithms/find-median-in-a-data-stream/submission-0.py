class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap,num)
        
    def findMedian(self) -> float:
        n = len(self.heap)
        if n%2==0:
            n=n//2 + 1
            removed = []
            for _ in range(n):
                removed.append(heapq.heappop(self.heap))
            
            ans = (removed[-1]+removed[-2])/2

            self.heap+=removed
            heapq.heapify(self.heap)

            return ans

        else:
            n=n//2 + 1
            removed = []
            for _ in range(n):
                removed.append(heapq.heappop(self.heap))
            
            ans = removed[-1]

            self.heap+=removed
            heapq.heapify(self.heap)

            return ans
        
        