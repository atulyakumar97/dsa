class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        hm = {}
        
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = pattern[i]
            else:
                if hm[s[i]] != pattern[i]:
                    return False
        
        if len(set(hm.values())) != len(hm.values()):
            return False
        
        return True
            