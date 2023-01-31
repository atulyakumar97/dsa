class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first = ""
        second = ""
        flag = True
        
        for char in word:
            
            if flag:
                first = char + first
                if char == ch:
                    flag = False
            else:
                second += char
        
        if flag:
            return word
        else:
            return first + second