from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid - 1] < target < nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return mid


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        h = len(nums) - 1
        
        while l <= h:
            m = (l + h) // 2
            
            # found -> return index
            if nums[m] == target:
                return m
            # not found -> less than first element
            elif m == 0 and nums[0] > target:
                return 0
            # not found -> greater than last element
            elif m == len(nums) - 1 and nums[len(nums)-1] < target:
                return len(nums)
            # not found -> previous element smaller and next element greater
            elif nums[m-1] < target and nums[m] > target:
                return m
            # not found -> reduce search area to first half of array
            elif nums[m] > target:
                h = m - 1
            # not found -> reduce search area to second half of array
            else:
                l = m + 1
