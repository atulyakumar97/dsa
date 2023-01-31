class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        m1 = - float('inf')
        m2 = - float('inf')
        m3 = - float('inf')
        
        for i in range(len(nums)):
            
            if nums[i] > m1:
                m3 = m2
                m2 = m1
                m1 = nums[i]
            elif nums[i] > m2 and nums[i] != m1:
                m3 = m2
                m2 = nums[i]
            elif nums[i] > m3 and nums[i] != m2 and nums[i] != m1:
                m3 = nums[i]
                
        if m3 == - float('inf'):
            return m1
        else:
            return m3
