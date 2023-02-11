from typing import List


def subarray_sum(arr: List[int], target: int) -> List[int]:
    prefix_sum = {0: 0}
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        complement = current_sum - target

        if complement in prefix_sum:
            return [prefix_sum[complement], i + 1]

        prefix_sum[current_sum] = i + 1
    return []


if __name__ == '__main__':
    arr = [1, -20, -3, 30, 5, 7]
    target = 7
    res = subarray_sum(arr, target)
    print(' '.join(map(str, res)))
