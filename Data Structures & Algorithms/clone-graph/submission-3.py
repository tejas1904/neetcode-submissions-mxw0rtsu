"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        node_to_new = {}
        def dfs(node):
            if node==None:
                return None
            if node in node_to_new:
                return node_to_new[node]
            else:
                newNode = Node(node.val)
                node_to_new[node] = newNode
                for nbr in node.neighbors:
                    ret = dfs(nbr)
                    if ret:
                        newNode.neighbors.append(ret)
                return newNode
                    
        return dfs(node)


        