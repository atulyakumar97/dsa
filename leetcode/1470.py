class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * 2 *n
        i = 0 
        j = n
        k = 0
        while k < 2*n:
            ans[k] = nums[i]
            k += 1
            ans[k] = nums[j]
            k += 1
            i += 1
            j += 1
                    
        return ans