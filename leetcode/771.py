class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict()
        for j in jewels:
            d[j] = True
        
        c = 0
        for s in stones:
            if d.get(s):
                c += 1
        
        return c
            