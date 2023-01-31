# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3 = None
        carry = 0
        
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            
            
            if l3 is None:       
                l3 = ListNode(sum % 10)
                curr = l3
            else:
                curr.next = ListNode(sum % 10)
                curr = curr.next      
                            
            l1 = l1.next
            l2 = l2.next
            
            carry = sum // 10
        
        while l1 is not None:
            
            sum = l1.val + carry            
            
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            l1 = l1.next
            
            carry = sum // 10
        
        while l2 is not None:
            
            sum = l2.val + carry
            
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            l2 = l2.next
            
            carry = sum // 10
        
        if carry != 0:            
            curr.next = ListNode(carry)
            
            
        return l3
            