from collections import Counter
from typing import List

class Solution:
    def subarraySum(self, arr: List[int], target: int) -> int:
        prefix_sum = Counter()
        prefix_sum[0] = 1  # empty subarray, count=1 for sum=0

        curr_sum = 0
        count = 0

        for i in range(len(arr)):
            curr_sum += arr[i]
            complement = curr_sum - target

            if complement in prefix_sum:
                # add count to overall count
                # these many sub arrays equals k
                count += prefix_sum[complement]

            prefix_sum[curr_sum] += 1  # increase counter of current sum

        return count
