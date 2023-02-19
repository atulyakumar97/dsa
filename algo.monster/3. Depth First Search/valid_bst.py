import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: Node) -> bool:
    def dfs(node, min_val, max_val):

        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, -math.inf, math.inf)


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter("6 4 3 x x 5 x x 8 x x".split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')
