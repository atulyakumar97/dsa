from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        hm = Counter(s)
        
        extra = ""
        
        for char in t:
            if char in hm and hm[char] > 0:
                hm[char] -= 1
            else:
                extra += char
        
        return extra
