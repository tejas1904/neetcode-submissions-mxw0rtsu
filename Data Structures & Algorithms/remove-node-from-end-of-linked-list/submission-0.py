# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def ReverseList(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
        
        head = ReverseList(head)

        tempHead = ListNode()
        tempHead.next = head

        prev = tempHead
        curr = head
        count = 1
        while count:
            if count==n:
               prev.next = curr.next
               break 
            prev = curr
            curr = curr.next
            count += 1
        
        return ReverseList(tempHead.next)

        
        
