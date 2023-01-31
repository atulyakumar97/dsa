class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        m = len(word1)
        
        j = 0
        n = len(word2)
        
        word3 = ""
        
        while i < m and j < n:
            
            word3 += word1[i] + word2[i]
            
            i += 1
            j += 1
            
        return word3 + word1[i:] + word2[j:]
