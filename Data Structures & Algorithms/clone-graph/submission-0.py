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
        origToCopy = {}
        queue = deque()
        
        head = Node()
        head.val = node.val
        
        origToCopy[node] = head

        queue.append(node)

        while queue:
            node_orig = queue.popleft()
            node_copy = origToCopy[node_orig]

            for orig_neighbor in node_orig.neighbors:
                nodeToAppend = None
                if orig_neighbor not in origToCopy.keys():
                    queue.append(orig_neighbor)

                    nodeToAppend = Node()
                    origToCopy[orig_neighbor] = nodeToAppend
                    nodeToAppend.val = orig_neighbor.val
                else:
                    nodeToAppend = origToCopy[orig_neighbor]
                    
                node_copy.neighbors.append(nodeToAppend)

        
        return head

            
        