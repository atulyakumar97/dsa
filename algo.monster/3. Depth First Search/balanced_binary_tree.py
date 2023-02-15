class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Node) -> bool:
    def dfs(node):

        if node is None:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        if left_height == -1 or right_height == -1:  # if left or right is unbalanced
            return -1  # unbalanced

        if abs(left_height - right_height) > 1:  # if left & right height differ by >1
            return -1  # unbalanced

        return max(left_height, right_height) + 1  # so far balanced

    if dfs(tree) == -1:
        return False
    else:
        return True


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    tree = build_tree(iter(['1', '2', '4', 'x', '7', 'x', 'x', '5', 'x', 'x', '3', 'x', '6', 'x', 'x']), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
