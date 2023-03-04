from typing import List
from heapq import heappush, heappop


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    heap = []
    min_count = 0

    for sub_list in matrix:
        heappush(heap, (sub_list[0], sub_list, 0))

    while min_count != k:
        val, arr, ptr = heappop(heap)
        min_count += 1
        if ptr + 1 < len(arr):
            heappush(heap, (arr[ptr + 1], arr, ptr + 1))

    return val


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    res = kth_smallest(matrix, k)
    print(res)
