class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {}
        for i in range(1, len(edges) + 1):
            adj_list[i] = []
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u) 
        
        visited = set()
        path = []
        self.cycle = None
        def dfs(node, parent):#return true if a cyle is found and the path is modified as well
            nonlocal path  # Declare first
            
            if node in visited: # if cylce detected return True
                # Find where the cycle starts in the DFS path
                # since node is in visited in the curent path there will be an edge from (node)->(something) 
                #this is cycle begining
                idx = 0
                while idx < len(path):
                    u,v = path[idx]
                    if u == node:  
                        break
                    idx += 1
                self.cycle = path[idx:] #extract that cycle
                self.cycle.append((parent, node))# Add the back edge that completes the cycle
                return True
            
            visited.add(node) 
            path.append((parent, node))
            for nbr in adj_list[node]:
                if nbr == parent:
                    continue
                if dfs(nbr, node):
                    return True
            path.pop()
            return False
        
        dfs(1, -1)
        self.cycle = set(self.cycle)
        for u, v in reversed(edges):
            if (u, v) in self.cycle or (v, u) in self.cycle: 
                return [u, v]