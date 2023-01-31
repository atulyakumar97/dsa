class Solution:
    def sortSentence(self, s: str) -> str:
        s1 = s.split(' ')
        size = len(s1)
        ans = [''] * size
        
        for word in s1:
            target = int(word[-1])
            ans[target-1] = word[:-1]
        
        return ' '.join(ans)
        
        