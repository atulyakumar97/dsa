class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    arr = []

    def dfs(node):
        if node is None:
            arr.append('x')
            return
        arr.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ' '.join(arr)


def deserialize(s):
    arr_iter = iter(s.split())

    def dfs(nodes):
        val = next(nodes)

        if val == 'x':
            return

        curr = Node(int(val))
        curr.left = dfs(nodes)
        curr.right = dfs(nodes)

        return curr

    return dfs(arr_iter)


if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur


    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)


    root = build_tree(iter("6 4 3 x x 5 x x 8 x x".split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))
