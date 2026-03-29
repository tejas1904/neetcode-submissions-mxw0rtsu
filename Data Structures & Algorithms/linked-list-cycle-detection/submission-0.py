# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = [head]
        visited = set()
        while stack:
            node = stack.pop(-1)
            visited.add(node)
            neighbour = node.next
            if neighbour not in visited: 
                if neighbour:
                    stack.append(neighbour)
            else:
                return True
        
        return False

            

        