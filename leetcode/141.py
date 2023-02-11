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
    def hasCycle(self, nodes: Optional[ListNode]) -> bool:

        if not nodes:
            return False

        slow = next_node(nodes)
        fast = next_node(next_node(nodes))

        while slow != fast and fast.next is not None:
            # exit condition = intersection or end
            slow = next_node(slow)
            fast = next_node(next_node(fast))

        if fast.next is None:
            # end reached -> no cycle
            return False
        else:
            # slow == fast -> intersection occurred
            return True
