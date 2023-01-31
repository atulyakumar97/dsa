class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        brokenLetters = set(brokenLetters)
        c = len(text)
        
        for word in text:
            for char in word:
                if char in brokenLetters:
                    c -= 1
                    break
                
        return c