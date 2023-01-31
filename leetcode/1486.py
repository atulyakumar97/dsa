class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(start, start + 2*n-1, 2):
            if i == start:
                continue
            else:
                ans = ans ^ i
        return ans
        