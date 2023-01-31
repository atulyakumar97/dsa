from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums2)
        
        intersection = []
        
        for val in nums1:
            if val in c and c[val] > 0:
                intersection.append(val)
                c[val] -= 1
        
        return intersection
