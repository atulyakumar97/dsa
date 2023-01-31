class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)
        
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
            if hm[num] >= n//2 + 1:
                return num
