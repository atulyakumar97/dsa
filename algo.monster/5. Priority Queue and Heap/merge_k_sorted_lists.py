from typing import List
import heapq


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    #     min_heap = []
    #     res = []

    #     for sub_list in lists:
    #         for item in sub_list:
    #             heapq.heappush(min_heap, item)

    #     for i in range(len(min_heap)):
    #         res.append(heapq.heappop(min_heap))

    heap = []
    res = []

    for sub_list in lists:
        heapq.heappush(heap, (sub_list[0], sub_list, 0))

    while heap:
        new_min, sub_list, pointer = heapq.heappop(heap)
        res.append(new_min)

        if pointer < len(sub_list) - 1:
            pointer += 1
            heapq.heappush(heap, (sub_list[pointer], sub_list, pointer))

    return res


if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))
