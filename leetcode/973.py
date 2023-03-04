from math import sqrt
from heapq import heappush, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for point in points:
            dist = sqrt(point[0] ** 2 + point[1] ** 2)
            heappush(heap, (dist, point))

        for _ in range(k):
            _, point = heappop(heap)
            res.append(point)

        return res
