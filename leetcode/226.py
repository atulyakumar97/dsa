from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        return TreeNode(
            val=root.val,
            left=Solution().invertTree(root.right),
            right=Solution().invertTree(root.left)
        )
