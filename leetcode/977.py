class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l = 0
        r = n - 1
        i = 0
        
        while r >= l and i!= n:
            if abs(nums[l]) > abs(nums[r]):
                ans[n-1-i] = nums[l]**2
                l += 1
            else:
                ans[n-1-i] = nums[r] ** 2
                r -= 1
            i += 1
        return ans
                