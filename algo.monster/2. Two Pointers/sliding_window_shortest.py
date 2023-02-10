from typing import List


def subarray_sum_shortest(nums: List[int], target: int) -> int:
    window_sum, length = 0, len(nums)
    left = 0

    for right in range(len(nums)):

        window_sum += nums[right]

        while window_sum >= target:
            length = min(length, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return length


if __name__ == '__main__':
    nums = [1, 4, 1, 7, 3, 0, 2, 5]
    target = 10
    res = subarray_sum_shortest(nums, target)
    print(res)
