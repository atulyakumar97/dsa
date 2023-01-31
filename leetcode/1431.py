class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_c = max(candies)
        ans = []
        
        for c in candies:
            if c + extraCandies >= max_c:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans