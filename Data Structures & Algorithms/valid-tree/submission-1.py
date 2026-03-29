class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}
        for node in range(n):
            adj_list[node] = []
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(node,parent):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour != parent:
                    if neighbour in visited:
                        return False
                    else:
                        ret  = dfs(neighbour,node)
                        if ret==False:
                            return False
            return True
        
        is_no_cycle =  dfs(0,-1)
        
        if set(range(n))==visited and is_no_cycle:
            return True
        else:
            return False

        

            

        