# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = None
        newNode = False
        sum = 0
        
        while head:
            
            if head.val == 0:
                if sum != 0:
                    if merged is None:
                        merged = ListNode(sum)
                        cur = merged
                    else:
                        cur.next = ListNode(sum)
                        cur = cur.next
                sum = 0
            
            sum += head.val
            head = head.next
        
        return merged