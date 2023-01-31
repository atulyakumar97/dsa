class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i, val in enumerate(nums):
            
            if val in hm:
                return [i, hm[val]]
            else:           
                hm[target - val] = i
