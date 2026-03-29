class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = {}
        for course in range(numCourses):
            graph[course] = []
            indegree[course] = 0
        
        for course,prereq in prerequisites:
            graph[course].append(prereq)
            indegree[prereq]+=1
        
        q = []
        for node in range(numCourses):
            if indegree[node]==0:
                q.append(node)
        
        while q:
            node = q.pop(0)
            for nbr in graph[node]:
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        for node in range(numCourses):
            if indegree[node]>0:
                return False
        return True

        
        

        