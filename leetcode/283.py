class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        j = len(nums) - 1
        
        while j >= 0:
            
            if nums[j] == 0:
                del nums[j]
                nums.append(0)
            
            j -= 1
