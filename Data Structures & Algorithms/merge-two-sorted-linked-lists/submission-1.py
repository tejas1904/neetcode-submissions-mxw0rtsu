# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start=ListNode()
        p1 = list1
        p2 = list2
        
        node = start

        while p1 and p2:
            if p1.val<=p2.val:
                node.next = p1
                node = node.next
                p1=p1.next
            elif p1.val>p2.val:
                node.next = p2
                node = node.next
                p2=p2.next
        
        while p1:
            node.next = p1
            node = node.next
            p1=p1.next
        while p2:
            node.next = p2
            node = node.next
            p2=p2.next
        
        return start.next


        