from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def next_node(nodes: ListNode) -> ListNode:
    if nodes.next:
        return nodes.next
    else:
        return nodes


class Solution:
    def detectCycle(self, nodes: Optional[ListNode]) -> Optional[ListNode]:
        if not nodes:
            return None

        seen = set()

        while nodes not in seen and nodes.next is not None:
            seen.add(nodes)
            nodes = next_node(nodes)

        if nodes.next is None:
            return None
        else:
            return nodes


class Solution2:
    def detectCycle(self, nodes: Optional[ListNode]) -> Optional[ListNode]:
        if not nodes:
            return None

        slow = fast = nodes

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = nodes
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
