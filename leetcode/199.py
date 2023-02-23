from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        ans = list()

        if root:
            queue.append(root)

        while len(queue) > 0:
            n = len(queue)
            ans.append(queue[-1].val)

            for _ in range(n):
                node = queue.popleft()

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        return ans
