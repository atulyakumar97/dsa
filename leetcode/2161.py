class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        big = []
        equal = []
        small = []
        
        for i in range(len(nums)):
            if nums[i] > pivot:
                big.append(nums[i])
            elif nums[i] < pivot:
                small.append(nums[i])
            else:
                equal.append(nums[i])
        
        return small + equal + big