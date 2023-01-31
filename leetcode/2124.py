class Solution:
    def checkString(self, s: str) -> bool:
        s = s.split('b')[1:]
        if len(s) == 0 or max(s) == '':
            return True
        else:
            return False
