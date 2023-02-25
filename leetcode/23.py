from heapq import heappush, heappop
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = head = None

        for linked_list in lists:
            if linked_list:
                heappush(heap, (linked_list.val, id(linked_list), linked_list))

        while heap:
            val, _, curr = heappop(heap)

            if not head:
                head = res = ListNode(val=val, next=None)
            else:
                res.next = ListNode(val=val, next=None)
                res = res.next

            if curr.next:
                curr = curr.next
                heappush(heap, (curr.val, id(curr), curr))

        del res, heap

        return head
