class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        
        for char in word1:
            c1 = w1[char]
            c2 = w2.get(char, 0)
            
            if c1 - c2 > 3:
                return False
        
        for char in word2:
            c1 = w1.get(char, 0)
            c2 = w2[char]
            
            if c2 - c1 > 3:
                return False
        
        return True