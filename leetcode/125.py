class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        actual = ""
        
        for char in s:
            if char.isalnum():
                rev = char.lower() + rev
                actual += char.lower()
            
        del s
        return rev == actual
