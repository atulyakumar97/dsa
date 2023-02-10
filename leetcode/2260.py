from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        window_hm = dict()
        window_size = 10 ** 5 + 1

        for right in range(len(cards)):
            window_hm[cards[right]] = window_hm.get(cards[right], 0) + 1

            while window_hm[cards[right]] > 1:
                window_size = min(window_size, right - left + 1)
                window_hm[cards[left]] -= 1
                left += 1

        if window_size == 10 ** 5 + 1:
            return -1

        return window_size
