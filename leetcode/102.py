from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:

            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()

                level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)

            ans.append(level)

        return ans
