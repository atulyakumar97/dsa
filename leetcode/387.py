from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hm = OrderedDict()
        
        for i in range(len(s)):
            hm[s[i]] = 1 + hm.get(s[i], 0)
        
        char = ""
        
        for key in hm.keys():
            if hm[key] == 1:
                char = key
                break
        
        for i in range(len(s)):
            if s[i] == char:
                return i
        
        return -1
        