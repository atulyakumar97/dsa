from collections import Counter

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        hm = Counter(allowed)
        c = 0
        
        for word in words:
            c += 1
            for char in word:
                if char not in hm:
                    c -= 1
                    break
        
        return c
            
        
        