from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = Counter(arr)
        freq = Counter(hm.values())
        
        for f in freq:
            if freq[f] > 1:
                return False
        
        return True