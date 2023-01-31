class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 1, 2, 2, 3, 8
        nums2 = sorted(nums)
        rank = {}
        
        for i in range(len(nums2)):
            if nums2[i] not in rank:
                rank[nums2[i]] = i
        
        ans = []
        for i in nums:
            ans.append(rank[i])
        
        return ans
                
            
        