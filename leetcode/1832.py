from collections import Counter

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence) < 26:
            return False
        
        hm = {}
        
        for char in sentence:
            hm[char] = 1
        
        
        return hm == Counter('abcdefghijklmnopqrstuvwxyz')