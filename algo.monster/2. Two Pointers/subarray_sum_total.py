from typing import List
from collections import Counter


def subarray_sum_total(arr: List[int], target: int) -> int:
    prefix_sum = Counter()
    prefix_sum[0] = 1  # empty subarray, count=1 for sum=0

    curr_sum = 0
    count = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        complement = curr_sum - target

        if complement in prefix_sum:
            # add count to overall count
            # these many sub arrays equals k
            count += prefix_sum[complement]

        prefix_sum[curr_sum] += 1  # increase counter of current sum

    return count


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_total(arr, target)
    print(res)
