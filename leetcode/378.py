from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for row in matrix:
            heappush(heap, (row[0], row, 0))

        count = 0

        while heap and count != k:
            val, row, ptr = heappop(heap)

            if ptr + 1 < len(row):
                heappush(heap, (row[ptr + 1], row, ptr + 1))

            count += 1

        return val
