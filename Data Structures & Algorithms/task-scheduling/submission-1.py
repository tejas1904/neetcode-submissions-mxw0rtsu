class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        heap = []

        for task in tasks:
            count[task] = count.get(task,0) + 1
        
        for task in count.keys():
            heapq.heappush( heap, (1,task) )

        t=1
        while heap:
            next_time, task = heap[0]

            if next_time<=t: #do the task
                count[task]-=1
                
                if count[task]!=0:
                    heap[0] = (next_time+n+1 , task)
                    heapq.heapify(heap)
                
                elif count[task]==0:
                    heapq.heappop(heap)
            
            t+=1
        
        return t-1

