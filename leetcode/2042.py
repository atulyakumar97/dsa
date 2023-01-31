class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')
        cur = 0

        for token in s:
            if token.isnumeric():
                next = int(token)
                if next > cur:
                    cur = next
                else:
                    return False
        
        return True
