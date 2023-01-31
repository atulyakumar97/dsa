class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        remove_index = set()
        
        for i in range(len(intervals)):
            a = intervals[i][0]
            b = intervals[i][1]
            for j in range(len(intervals)):
                if i != j:
                    c = intervals[j][0]
                    d = intervals[j][1]
                    if c <= a and b <= d:
                        remove_index.add(i)
                    
        return len(intervals) - len(remove_index)

    # a,b
    # c,d
    