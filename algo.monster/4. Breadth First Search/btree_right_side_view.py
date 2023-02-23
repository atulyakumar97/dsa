from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: Node) -> List[int]:
    queue = deque([root])
    ans = list()

    while len(queue) > 0:
        n = len(queue)
        ans.append(queue[-1].val)

        for _ in range(n):
            node = queue.popleft()

            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

    return ans


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter("1 2 4 x 7 x x 5 x x 3 x 6 x x".split()), int)
    res = binary_tree_right_side_view(root)
    print(' '.join(map(str, res)))
