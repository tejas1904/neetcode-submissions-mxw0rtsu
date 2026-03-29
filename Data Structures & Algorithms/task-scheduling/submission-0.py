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
            next_time, task = heapq.heappop(heap)

            if next_time<=t: #do the task
                count[task]-=1
                
                if count[task]!=0:
                    heapq.heappush(heap, (next_time+n+1 , task))

            else:
                heapq.heappush(heap,(next_time,task)) 
            
            t+=1
        
        return t-1

