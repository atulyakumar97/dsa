class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0       
        for sen in sentences:
            words = sen.split(' ')
            if len(words) > max:
                max = len(words)
        return max