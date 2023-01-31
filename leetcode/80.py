class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hm = {}
        
        for i in range(len(nums)):
            hm[nums[i]] = 1 + hm.get(nums[i], 0)
            
        j = len(nums) - 1
        
        while j>=0:
            if hm.get(nums[j], 0) > 2:
                hm[nums[j]] -= 1
                del nums[j]
            j -= 1
        
        return len(nums)
            
            
        