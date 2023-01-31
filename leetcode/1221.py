class Solution:
    def balancedStringSplit(self, s: str) -> int:
        t = ""
        r = 0
        l = 0
        c = 0
        
        for char in s:
            t += char
            
            if char == 'R':
                r += 1
            else:
                l += 1
            
            if l == r:
                c += 1
                t = ""
        
        return c
            