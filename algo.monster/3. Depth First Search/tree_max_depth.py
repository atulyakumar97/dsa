class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # depth of current node's subtree = max depth of the two subtrees + 1 provided by current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root) - 1 if root else 0


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter([5, 4, 3, 'x', 'x', 8, 'x', 'x', 6, 'x', 'x']), int)
    res = tree_max_depth(root)
    print(res)
