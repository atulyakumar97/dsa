from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_min_depth(root: Node) -> int:
    queue = deque([root])
    depth = 0

    while len(queue) > 0:
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        depth += 1


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter("1 2 4 x 7 x x 5 x x 3 x 6 x x".split()), int)
    res = binary_tree_min_depth(root)
    print(res)
