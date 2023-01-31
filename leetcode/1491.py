class Solution:
    def average(self, salary: List[int]) -> float:
        
        max = - float('inf')
        min = float('inf') 
        total = 0
        
        for s in salary:
            if s > max:
                max = s
            
            if s < min:
                min = s
            
            total += s
        
        
        return (total - max - min)/(len(salary) - 2)
