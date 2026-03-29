# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = ListNode()
        prev = None
        currnode = head

        while currnode != None:
            tempNode.next = currnode.next
            currnode.next =  prev
            prev = currnode
            currnode = tempNode.next
        
        return prev
