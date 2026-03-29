# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        curr1, curr2 = l1,l2

        newhead = ListNode()
        ptr = newhead

        while curr1 or curr2:
            
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            
            summ = val1 + val2 + carry
            digit = summ%10
            carry = summ // 10 

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            
            ptr.next = ListNode(digit)
            ptr = ptr.next 

        if carry!=0:
            ptr.next = ListNode(carry)
            ptr = ptr.next 

        ret = newhead.next
        return ret
            
            
            

        