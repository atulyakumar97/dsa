from typing import List
from heapq import heappush, heappop


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []
        res = []

        for i in range(k):
            dist = abs(arr[i] - x)
            heappush(heap, (-dist, arr[i]))

        for i in range(k, len(arr)):
            dist = abs(arr[i] - x)
            if dist < - heap[0][0]:
                heappop(heap)
                heappush(heap, (-dist, arr[i]))

        for i in range(k):
            res.append(heap[i][1])

        return sorted(res)
