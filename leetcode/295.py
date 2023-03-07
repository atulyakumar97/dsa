from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.l_max_heap = []
        self.r_min_heap = []

    def addNum(self, num: int) -> None:

        l = len(self.l_max_heap)
        r = len(self.r_min_heap)

        # add to left if right is empty
        # add to left if num less than right heap min
        if r == 0 or num < self.r_min_heap[0]:
            heappush(self.l_max_heap, -num)
        else:
            heappush(self.r_min_heap, num)

        self._balance()

    def _balance(self):

        l = len(self.l_max_heap)
        r = len(self.r_min_heap)

        # left heap should always be greater than right
        # move one element to left if it's not
        if l < r:
            val = heappop(self.r_min_heap)
            heappush(self.l_max_heap, -val)

        # difference between len left and right
        # heap should not exceed 1
        if l > r + 1:
            val = - heappop(self.l_max_heap)
            heappush(self.r_min_heap, val)

    def findMedian(self) -> float:

        if len(self.l_max_heap) == len(self.r_min_heap):
            return (-self.l_max_heap[0] + self.r_min_heap[0]) / 2

        return -self.l_max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
