from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        head = Node(node.val)
        origToCopy = {}

        origToCopy[node] = head
        queue = deque([node])

        while queue:
            node_orig = queue.popleft()
            node_copy = origToCopy[node_orig]

            for orig_neighbor in node_orig.neighbors:
                if orig_neighbor not in origToCopy:
                    origToCopy[orig_neighbor] = Node(orig_neighbor.val)
                    queue.append(orig_neighbor)
                
                node_copy.neighbors.append(origToCopy[orig_neighbor])

        return origToCopy[node]
