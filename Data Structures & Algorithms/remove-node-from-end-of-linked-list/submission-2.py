# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev,slow,fast = dummy,head,head

        # fast n times
        for _ in range(n):
            fast  = fast.next
        #fast in now n nodes ahead of slow
        
        #move fast until it reachs the None After end 
        #now slow will be n nodes behind last node (fast pointer)
        while fast:
            prev = prev.next
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        
        return dummy.next
        

        

        