# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def Reverse(head):
            prev,curr = None,head
            while curr:
                nxt = curr.next
                curr.next  = prev
                prev = curr
                curr = nxt
            return prev
        
        
        newhead = ListNode(0,next=head)

        start,curr = newhead,newhead
        i=0
        while curr.next:
            curr = curr.next
            i+=1

            if i%k == 0:
                nxt = curr.next
                grp_begin  = start.next
                grp_end = curr
                
                grp_end.next = None
                Reverse(grp_begin)
                
                start.next = grp_end
                grp_begin.next = nxt
                
                start = grp_begin
                curr = grp_begin
                i=0

        return newhead.next
                


        
        