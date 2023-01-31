class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        half = len(s) // 2
        c1 = 0
        c2 = 0
        
        for i in range(len(s)):
            is_vowel = self.isVowel(s[i], v)
            if i < half and is_vowel:
                c1 += 1
            elif i>= half and is_vowel:
                c2 += 1        
        return c1 == c2
                
    def isVowel(self, x, v):
         
        if x in v:
            return True
        else:
            return False