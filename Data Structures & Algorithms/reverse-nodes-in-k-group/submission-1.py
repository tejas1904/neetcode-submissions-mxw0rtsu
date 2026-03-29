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
        #start is the node before a group of k nodes
        while curr.next:
            curr = curr.next
            i+=1

            if i%k == 0:
                #curr is now pointing to end of a group
                grp_begin  = start.next
                grp_end = curr

                #first node after the group
                nxt = curr.next
                
                #detach and reverse the group
                grp_end.next = None
                Reverse(grp_begin)
                
                #grup end is now the begining and the start is the end
                start.next = grp_end
                grp_begin.next = nxt
                
                #reset
                start = grp_begin
                curr = grp_begin
                i=0

        return newhead.next
                


        
        