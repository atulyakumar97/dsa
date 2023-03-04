from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev = None
        curr = None

        while head:
            prev = ListNode(head.val)
            prev.next = curr
            curr = prev

            head = head.next

        return prev


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev = None  # last node

        while head:
            curr = head  # store current
            curr.next = prev  # assign prev node as next node
            prev = curr  # make current node as previous node

            head = head.next  # goto next

        return prev
