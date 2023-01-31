class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        sum = 0
        
        for i in gain:
            sum += i
            if sum > alt:
                alt = sum
        
        return alt