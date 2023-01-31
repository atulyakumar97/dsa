from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hm = {}
        
        for char in s1:
            hm[char] = 1 + hm.get(char, 0)
        
        i = 0
        x = len(s1)
        
        
        while i < len(s2) - x + 1:
            y = Counter(s2[i:i+x])
            if y == hm:
                return True
            
            i += 1
        
        return False
                   
            