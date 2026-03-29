# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        slow=head
        fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse [mid to end]
        prev,curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        second = prev

        while second.next:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second=t2


        


        