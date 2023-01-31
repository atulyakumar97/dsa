class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        j = len(nums) - 1
        
        while j >= 0:
            if nums[j] == val:
                del[nums[j]]
        
            j -= 1
        
        return len(nums)