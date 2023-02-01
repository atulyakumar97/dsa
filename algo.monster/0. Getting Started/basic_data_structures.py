"""Basic Data Structure Templates"""

import math

# Array Enumerate

nums = [0, 10, 20, 30, 40, 50]
for i, num in enumerate(nums):
    print(i, num)

# Linked List


class LinkedListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        # append O(1)
        # find O(N)


# Stack - Python List - push, pop, len, top - O(1)
# Queue - Collections deque - append, popleft, len - O(1)
# Hash Table - Python Dict - get, set, del - O(1)
# Hash Set - Python Set - add, remove, exists - O(1)

class TreeNode:  # Binary Tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeNode:  # n-nary trees
    def __init__(self, val):
        self.val = val
        self.children = []


positive_inf = float('inf')
negative_inf = float('-inf')
positive_inf = math.inf
negative_inf = -math.inf