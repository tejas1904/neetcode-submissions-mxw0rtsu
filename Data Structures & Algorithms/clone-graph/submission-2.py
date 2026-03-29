"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None
        origToNew = {}

        def dfs(node):
            if node in origToNew:
                return origToNew[node]

            copy = Node(node.val)
            origToNew[node] = copy
            for origNeighbor in node.neighbors:
                copy.neighbors.append(dfs(origNeighbor))
            
            return copy
        
        return dfs(node)
        