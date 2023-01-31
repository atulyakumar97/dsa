class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 0
        index = set()
        
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i!=j and nums[i] == nums[j]:
                    if i * j % k == 0:
                        c += 1
                    
        return c
        