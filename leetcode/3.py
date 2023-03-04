class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        hm = dict()
        max_len = 0

        for r in range(len(s)):

            hm[s[r]] = hm.get(s[r], 0) + 1

            while hm.get(s[r]) > 1:
                hm[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
