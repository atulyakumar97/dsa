from typing import List
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root: Node) -> List[List[int]]:
    ans = list()
    queue = deque([root])
    rev = False

    while len(queue) > 0:
        n = len(queue)
        new_level = list()

        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)

            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

        if rev:
            ans.append(new_level[::-1])
        else:
            ans.append(new_level)

        rev = not rev

    return ans


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter("1 2 4 8 x x 9 x x 5 10 x x x 3 6 x 11 x x 7 12 x x 13 x x".split()), int)
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
