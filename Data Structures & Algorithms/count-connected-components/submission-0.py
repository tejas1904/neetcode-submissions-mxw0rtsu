class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #convert to adjacenty list
        adj_list={}
        for node in range(n):
            adj_list[node] = []
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        
        visited = set()
        components = 0

        for node in range(n):
            if node not in visited:
                #do a BFS
                queue = deque()
                queue.append(node)
                while queue:
                    n = queue.pop()
                    visited.add(n)
                    for neighbour in adj_list[n]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                
                components+=1
        
        return components
        