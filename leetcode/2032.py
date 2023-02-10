from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        n3 = set(nums3)

        return list(n1.intersection(n2).union(n2.intersection(n3)).union(n1.intersection(n3)))
