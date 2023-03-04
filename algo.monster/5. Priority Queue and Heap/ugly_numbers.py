from heapq import heappush, heappop


def nth_ugly_number(n: int) -> int:
    heap = [1]
    seen = {1}
    nums = [2, 3, 5]

    for _ in range(n - 1):
        heap_min = heappop(heap)

        for num in nums:
            ugly_num = heap_min * num
            if ugly_num not in seen:
                heappush(heap, ugly_num)
                seen.add(ugly_num)

    return heap[0]


if __name__ == '__main__':
    n = int(input())
    res = nth_ugly_number(n)
    print(res)
