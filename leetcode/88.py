import numpy as np

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while k >= 0 and j >= 0 and i >= 0:
            
            # compare and place the largest element at end of 1st array
            if nums2[j] <= nums1[i]:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        
        # insert remaining elements if first list gets over
        
        while k >= 0 and j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        return nums1
                
            
        