# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        h = n
        l = 0
        
        while l <= h:
            m = (l + h) // 2
            
            current = isBadVersion(m)
            previous = isBadVersion(m - 1)
                        
            if current and not previous:
                return m
            elif not current and not previous:
                l = m + 1
            else:
                h = m - 1    
                            
                