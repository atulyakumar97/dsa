class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = 0
        i = len(columnTitle) - 1
        for char in columnTitle:
            col += (ord(char) - ord('A') + 1) * 26 ** i
            i -= 1
        
        return col
