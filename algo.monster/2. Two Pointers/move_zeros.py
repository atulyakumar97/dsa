from typing import List


def move_zeros(nums: List[int]) -> None:
    slow = 0  # stop at next zero
    for fast in range(len(nums)):

        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1

    pass


if __name__ == '__main__':
    nums = [1, 0, 2, 0, 0, 7]
    move_zeros(nums)
    print(' '.join(map(str, nums)))
