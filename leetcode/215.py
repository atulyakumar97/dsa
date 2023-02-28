from typing import List
from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for i in range(k):
            heappush(heap, nums[i])

        for j in range(k, len(nums)):
            if nums[j] > heap[0]:
                heappop(heap)
                heappush(heap, nums[j])

        return heappop(heap)
