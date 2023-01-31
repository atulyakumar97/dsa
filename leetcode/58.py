class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        r = len(s) - 1
        started = False
        count = 0
        
        while r >= 0:
            if s[r].isspace() and started:
                break
            elif s[r].isspace():
                r -= 1
                continue
            elif s[r].isalpha():
                if not started:
                    started = True
                count += 1
                r -= 1
        
        return count
                
        