class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        
        s = list(s)
        
        while i < j:
            while not s[i].isalpha() and i<j:
                i += 1
            while not s[j].isalpha() and i<j:
                j -= 1
            
            (s[i], s[j]) = (s[j], s[i])
            
            i += 1
            j -= 1
        
        return ''.join(s)