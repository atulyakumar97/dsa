from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = list()
        rev = False

        if root:
            queue.append(root)

        while len(queue) > 0:
            n = len(queue)
            level = list()

            for _ in range(n):
                node = queue.popleft()
                if not rev:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

            ans.append(level)
            rev = not rev

        return ans
