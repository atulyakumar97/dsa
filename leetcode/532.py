class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        hm = {}
        count = 0
        
        for i in range(len(nums)):
            hm[nums[i]] = 1 + hm.get(nums[i], 0)
        
        if k == 0:
            for key, val in hm.items():
                if val > 1:
                    count += 1
        else:
            for key in hm:           
                if key + k in hm:
                    count += 1
            
        return count
