from typing import List
from heapq import heapify, heappop, heappush


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        heapify(nums)

        while len(nums) > k:
            heappop(nums)

        self.nums = nums

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)

        if self.nums:
            return self.nums[0]

        return []


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
