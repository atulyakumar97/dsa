class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if n == 1:
            return True
        
        increasing = None
        
        for i in range(n-1):
            
            if increasing is None and nums[i] > nums[i+1]:
                increasing = False
            elif increasing is None and nums[i] < nums[i+1]:
                increasing = True
                        
            if increasing and nums[i] > nums[i+1]:
                return False
            
            if increasing == False and nums[i] < nums[i+1]:
                return False
                       
        return True

        
        