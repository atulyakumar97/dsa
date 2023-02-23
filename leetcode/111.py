from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            n = len(queue)
            depth += 1

            for _ in range(n):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    return depth

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        return depth
