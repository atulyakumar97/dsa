from typing import List


def subarray_sum_fixed(nums: List[int], k: int) -> int:
    current_sum = sum(nums[0:k])
    max_sum = 0

    for i in range(k, len(nums)):
        current_sum = current_sum + nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


if __name__ == '__main__':
    nums = [1, 2, 3, 7, 4, 1]
    k = 3
    res = subarray_sum_fixed(nums, k)
    print(res)
