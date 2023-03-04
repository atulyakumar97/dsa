from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        open = {'(', '[', '{'}
        close = {')', ']', '}'}
        open_close = {'()', '[]', '{}'}

        stack = deque()

        for char in s:
            if char in open:
                stack.append(char)

            if char in close:

                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if popped + char not in open_close:
                    return False

        if len(stack) > 0:
            return False

        return True
