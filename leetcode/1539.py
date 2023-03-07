from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        current = 1
        missing = 0

        for i in range(len(arr)):

            while current != arr[i]:
                missing += 1

                if missing == k:
                    return current

                current += 1

            current += 1

        for i in range(k - missing - 1):
            current += 1

        return current
