class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        start, end= s.split(':')
        start_alpha = start[0]
        start_index = int(start[1])
        end_alpha = end[0]
        end_index = int(end[1])
        
        ans = []
        
        for char in range(ord(start_alpha), ord(end_alpha)+1):
            for index in range(start_index, end_index+1):
                ans.append(chr(char) + str(index))
        
        return ans
