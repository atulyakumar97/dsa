from collections import Counter
from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:

        hm = Counter(s)
        heap = []
        n = len(s)

        for char, freq in hm.items():
            heappush(heap, (-freq, char))

        if -heap[0][0] > (n + 1) // 2:
            return ""

        ptr = 0
        res = [""] * n
        while heap:
            freq, char = heappop(heap)
            for i in range(-freq):
                res[ptr] = char
                ptr += 2
                if ptr >= n:
                    ptr = 1

        return "".join(res)
