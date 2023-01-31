class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        c = Counter(nums)  
        next = original
        
        while True:
            if next in c:
                next *= 2
            else:
                return next
                