from typing import List


def subarray_sum_longest(arr: List[int], target: int) -> int:
    left, right = 0, 0
    sub_sum = arr[0]
    max_len = 0

    while right < len(arr) - 1:

        right += 1
        sub_sum += arr[right]

        while sub_sum > target:
            sub_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 10, 0, 0, 0]
    target = 10
    res = subarray_sum_longest(nums, target)
    print(res)
