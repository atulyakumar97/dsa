class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        lines = [""] * numRows
        
        c = cycle(itertools.chain(range(numRows), range(numRows -2 , 0, -1)))
        
        for char in s:            
            lines[next(c)] += char            
        
        return ''.join(lines)
        
        