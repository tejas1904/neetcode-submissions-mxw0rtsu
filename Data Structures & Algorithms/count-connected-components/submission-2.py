class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for node in range(n):
            adj_list[node] = []

        for src,dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        components = 0
        
        seenNodes = set()
        for node in adj_list.keys():
            if node in seenNodes:
                continue

            #bfs
            components += 1
            queue = [node]
            seenNodes.add(node)
            
            while queue:
                for i in range(len(queue)):
                    node = queue.pop(0)
                    for nbr in adj_list[node]:
                        if nbr not in seenNodes:
                            queue.append(nbr)
                            seenNodes.add(nbr)
        
        return components



