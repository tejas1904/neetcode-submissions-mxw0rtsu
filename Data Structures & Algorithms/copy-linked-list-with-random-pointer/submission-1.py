"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}

        curr = head
        while curr:
            newNode = Node(curr.val)
            hm[curr] = newNode
            curr  = curr.next
        
        curr = head
        while curr:
            newnode = hm[curr]
            newnode.next = hm.get(curr.next, None)
            newnode.random = hm.get(curr.random, None)

            curr = curr.next
        
        return hm.get(head,None)
        
        