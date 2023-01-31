class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hm1 = {}
        for word in words1:
            hm1[word] = 1 + hm1.get(word, 0)
        
        hm2 = {}
        
        for word in words2:
            hm2[word] = 1 + hm2.get(word, 0)

        c = 0
        
        for word in hm1.keys():
            if hm1[word] == 1 and word in hm2 and hm2[word] == 1:
                c += 1
        
        return c