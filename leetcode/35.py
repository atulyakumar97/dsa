class Solution:
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
