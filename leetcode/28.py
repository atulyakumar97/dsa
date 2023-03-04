class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for i in range(n - m + 1):

            if haystack[i:i + m] == needle:
                return i

        return -1