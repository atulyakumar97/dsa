from typing import List
from heapq import heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) >= 2:
            s1 = heappop(heap)
            s2 = heappop(heap)

            new_stone = abs(s1 - s2)
            if new_stone > 0:
                heappush(heap, -new_stone)

        if not heap:
            return 0

        return -heap[0]
