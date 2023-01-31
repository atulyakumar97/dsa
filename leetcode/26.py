class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j = len(nums) - 1
        
        hm = {}
        
        while j>=0:
            hm[nums[j]] = 1 + hm.get(nums[j], 0)
            
            if hm[nums[j]] > 1:
                hm[nums[j]] -= 1
                del nums[j]
            
            j -= 1
        
        return len(nums)
                