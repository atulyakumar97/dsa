import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_val):

            if root is None:
                return 0

            total = 0

            if root.val >= max_val:
                total += 1
                max_val = max(root.val, max_val)

            total += dfs(root.left, max_val)
            total += dfs(root.right, max_val)

            return total

        return dfs(root, -math.inf)
