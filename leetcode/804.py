class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = {}
        
        for word in words:
            transform = ""
            for char in word:
                transform += map[ord(char) - 97]
            if transform not in ans:
                ans[transform] = 1
        
        return len(ans.keys())