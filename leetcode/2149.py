class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        i = 0 # positives
        j = 1 # negatives
        
        for num in nums:
            if num > 0:
                ans[i] = num
                i += 2
            else:
                ans[j] = num
                j += 2             
  
        return ans
