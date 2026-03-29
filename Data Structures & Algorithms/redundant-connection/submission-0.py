class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        for i in range(1,len(edges)+1):
            parent[i]  = i
        
        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while x!=root:
                up_x = parent[x]
                parent[x] = root
                x = up_x
            return root
        
        def union(u,v):
            if find(u)==find(v):
                return False
            else:
                p1 = find(u)
                p2 = find(v)
                parent[p2]=p1
        
        redundant = []
        for u,v in edges:
            ret = union(u,v)
            if ret==False:
                redundant.append([u,v])
        
        return redundant[-1]


        