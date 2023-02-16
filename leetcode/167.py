from typing import List


class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(arr)):
            complement = target - arr[i]
            if complement in hm:
                return [hm[complement], i + 1]
            hm[arr[i]] = i + 1

        return []


class Solution2:
    def twoSum(self, arr: List[int], target: int) -> List[int]:

        low = 0
        high = len(arr) - 1

        while high > low:

            if arr[high] + arr[low] == target:
                return [low + 1, high + 1]
            elif arr[high] + arr[low] > target:
                high -= 1
            else:
                low += 1

        return []

