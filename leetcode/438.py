from typing import List


class Solution:
    def findAnagrams(self, original: str, check: str) -> List[int]:
        check_hm = dict()

        for char in check:
            if char in check_hm:
                check_hm[char] += 1
            else:
                check_hm[char] = 1

        k = len(check)
        ans = []

        window = original[0: k]
        window_hm = dict()

        for char in window:
            if char in window_hm:
                window_hm[char] += 1
            else:
                window_hm[char] = 1

        if check_hm == window_hm:
            ans.append(0)

        for i in range(k, len(original)):

            add_char = original[i]
            del_char = original[i - k]

            if add_char in window_hm:
                window_hm[add_char] += 1
            else:
                window_hm[add_char] = 1

            window_hm[del_char] -= 1
            if window_hm[del_char] == 0:
                del window_hm[del_char]

            if window_hm == check_hm:
                ans.append(i - k + 1)

        return ans
