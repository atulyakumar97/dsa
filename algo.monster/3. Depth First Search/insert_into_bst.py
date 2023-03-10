class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_bst(bst: Node, val: int) -> Node:
    if bst is None:
        return Node(val=val)

    if val < bst.val:
        bst.left = insert_bst(bst.left, val)
    elif val > bst.val:
        bst.right = insert_bst(bst.right, val)

    return bst


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)


if __name__ == '__main__':
    bst = build_tree(iter("8 4 2 1 x x 3 x x 6 x x 12 10 x x 14 x 15 x x".split()), int)
    val = 7
    res = insert_bst(bst, val)
    print(' '.join(format_tree(res)))
