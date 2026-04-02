"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        orig_to_copy = {}
        def clone(origNode):
            if origNode in orig_to_copy:
                return orig_to_copy[origNode]
            elif origNode==None:
                return None
            else:
                newnode = Node(origNode.val)
                orig_to_copy[origNode] = newnode
                for nbr in origNode.neighbors:
                    ret = clone(nbr)
                    if ret!=None:
                        newnode.neighbors.append(ret)
                return newnode
        
        return clone(node)
        