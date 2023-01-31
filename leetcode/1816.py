from collections import defaultdict

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        c = 0
        for i in range(len(s)):
            if s[i] == " ":
                c += 1
                if c == k:
                    break
        if i + 1 == len(s):
            return s
        else:
            return s[:i]
                    
        