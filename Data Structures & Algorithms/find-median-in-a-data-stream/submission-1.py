class MedianFinder:

    def __init__(self):
        self.maxheap = []  # smaller half (stored as negatives)
        self.minheap = []  # larger half

    def Lheap(self, operation, num=None):
        if operation == 'push':
            heapq.heappush(self.maxheap, -num)
        elif operation == 'pop':
            return -heapq.heappop(self.maxheap)
        elif operation == 'peek':
            return -self.maxheap[0]
        elif operation == 'len':
            return len(self.maxheap)

    def Rheap(self, operation, num=None):
        if operation == 'push':
            heapq.heappush(self.minheap, num)
        elif operation == 'pop':
            return heapq.heappop(self.minheap)
        elif operation == 'peek':
            return self.minheap[0]
        elif operation == 'len':
            return len(self.minheap)

    def addNum(self, num: int) -> None:
        # put into left heap by default
        self.Lheap("push", num)

        # maintain ordering
        if self.Rheap("len")>0 and num >= self.Rheap("peek"):
            val = self.Lheap("pop")
            self.Rheap("push", val)

        # balance sizes
        if self.Lheap("len") > self.Rheap("len") + 1:
            self.Rheap("push", self.Lheap("pop"))
        elif self.Rheap("len") > self.Lheap("len"):
            self.Lheap("push", self.Rheap("pop"))

    def findMedian(self) -> float:
        if self.Lheap("len") == self.Rheap("len"):
            return (self.Lheap("peek") + self.Rheap("peek")) / 2
        elif self.Lheap("len") > self.Rheap("len"):
            return self.Lheap("peek")
        else:
            return self.Rheap("peek")
