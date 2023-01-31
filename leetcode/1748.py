class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        sum = 0
        
        for key in c:
            if c[key] == 1:
                sum += key
        
        return sum
