class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        for pair in prerequisites:
            pair[0],pair[1] = pair[1],pair[0]

        dv = [0 for i in range(numCourses)]
        for u,v in prerequisites:
            dv[v]+=1
        
        queue=[]
        op = []
        for i in range(len(dv)):
            if dv[i]==0:
                queue.append(i)
                dv[i]-=1
        
        while queue:
            node = queue.pop(0)
            op.append(node)

            for u,v in prerequisites:
                if u==node:
                    dv[v]-=1
            for i in range(len(dv)):
                if dv[i]==0:
                    queue.append(i)
                    dv[i]-=1
        
        if len(op)==numCourses:
            return op
        else:
            return []

