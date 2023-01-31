class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        i = 0
        
        good = 0
        
        while i < len(s) - 3 + 1:
            
            if len(set(s[i:i+3])) == 3:
                good += 1
        
            i += 1
        
        return good