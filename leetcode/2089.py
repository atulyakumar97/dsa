class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        
        for i, val in enumerate(nums):
            if target == val:
                indices.append(i)
        
        return indices