# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nonNullhead = 0
        for head in lists:
            if head:
                nonNullhead += 1

        newHead = ListNode()
        curr = newHead

        while nonNullhead>0:
            minhead = None
            minval = float('inf')
            minpos = 0

            pos = 0
            for head in lists:
                if head and head.val<minval:
                    minhead = head
                    minval = head.val
                    minpos = pos
                pos+=1
                
            curr.next = minhead
            minhead = minhead.next
            lists[minpos] = minhead
            curr = curr.next

            if minhead==None:
                nonNullhead-=1
        
        curr.next = None
        return newHead.next



        