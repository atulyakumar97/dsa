from heapq import heappop, heappush
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = res = ListNode()

        while list1 and list2:

            if list1.val <= list2.val:
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next
            else:
                res.next = ListNode(list2.val)
                res = res.next
                list2 = list2.next

        if list1:
            res.next = list1
        else:
            res.next = list2

        return head.next
