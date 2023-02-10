from typing import List
import math


def least_consecutive_cards_to_match(cards: List[int]) -> int:
    left = 0
    window_hm = dict()
    window_size = math.inf

    for right in range(len(cards)):
        window_hm[cards[right]] = window_hm.get(cards[right], 0) + 1

        while window_hm[cards[right]] > 1:
            window_size = min(window_size, right - left + 1)
            window_hm[cards[left]] -= 1
            left += 1

    if window_size == math.inf:
        return -1

    return window_size


if __name__ == '__main__':
    cards = [3, 4, 2, 3, 4, 7]
    res = 4
    print(res)
