class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for course in range(numCourses):
            graph[course] = []
        for course,prereq in prerequisites:
            graph[course].append(prereq)
        
        currentPath = set()
        def dfs(node):
            if node in currentPath:
                return False
            if graph[node] == []:
                return True
            
            currentPath.add(node)
            for neighbour in graph[node]:
                if dfs(neighbour)==False:
                    return False

            currentPath.remove(node)

    
        for i in range(0,numCourses):
            if dfs(i)==False:
                return False
        return True

        