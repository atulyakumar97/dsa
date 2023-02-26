from heapq import heappush, heappop
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res_head = res = ListNode()
        heap = []

        while head:
            heappush(heap, head.val)
            head = head.next

        while heap:
            val = heappop(heap)
            res.next = ListNode(val=val, next=None)
            res = res.next

        return res_head.next
