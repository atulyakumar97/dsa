from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                i += 2
                j += 2
            else:
                break

        return nums[i]