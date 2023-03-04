from heapq import heappush, heappop


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        heap = [1]
        seen = {1}
        nums = (2, 3, 5)

        for _ in range(n - 1):
            val = heappop(heap)
            for num in nums:
                ugly_num = val * num
                if ugly_num not in seen:
                    heappush(heap, ugly_num)
                    seen.add(ugly_num)

        return heap[0]
