class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(tree: Node) -> [Node, None]:
    if tree is None:
        return tree

    return Node(val=tree.val,
                left=invert_binary_tree(tree.right),
                right=invert_binary_tree(tree.left))


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
    tree = build_tree(iter("6 11 x 27 17 x x 23 x x 10 12 x x 13 x 14 x x".split()), int)
    res = invert_binary_tree(tree)
    print(' '.join(format_tree(res)))
