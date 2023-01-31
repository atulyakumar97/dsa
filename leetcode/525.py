class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        longest_subarray = 0
        hm = {}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
            
            if sum == 0:
                if i+1 > longest_subarray:
                    longest_subarray = i + 1
            elif sum in hm:
                if (i - hm[sum]) > longest_subarray:
                    longest_subarray = i - hm[sum]
            else:
                hm[sum] = i
                                
        return longest_subarray