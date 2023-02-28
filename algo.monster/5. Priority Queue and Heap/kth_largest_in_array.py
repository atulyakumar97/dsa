from typing import List
from heapq import heappush, heappop, heapreplace


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []

    for i in range(k):
        heappush(heap, nums[i])  # O(klogk)

    for j in range(k, len(nums)):  # O(n)
        if nums[j] > heap[0]:
            heappop(heap)  # O(nlogk)
            heappush(heap, nums[j])  # O(nlogk)  == O(n

    return heappop(heap)


if __name__ == '__main__':
    nums = [int(x) for x in "24 22 19 17 14 11 9 7 6 3 2 1".split()]
    k = 7
    res = find_kth_largest(nums, k)
    print(res)
